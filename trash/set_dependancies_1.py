####Wed 11 Jul 2012 08:31:01 PM IST 

from dbconnect import DBConnect



def setDependancies():
		
		pkg_idMap = {}
		new_pkg_idList = ''
		dependancyIdList = ''
		depSqlText = "INSERT DELAYED INTO dependancies ( main_soft_id, dep_soft_id ) VALUES "
		pkgSqlText = "INSERT DELAYED IGNORE INTO software ( package , soft_id ) VALUES "
		count = 0

		DB = 'softcenter'
		DB_HOST = 'localhost'
		DB_USER = 'root'
		DB_PASSWORD = '1'
		conn = MySQLdb.Connection(db=DB, host=DB_HOST, user=DB_USER,passwd=DB_PASSWORD)
		
		print("setDependancies.py started")
		cursor = conn.cursor()
		sql = "SELECT package,soft_id,depends FROM software"
		cursor.execute(sql)
		results = cursor.fetchall()
		cursor.close()
		
		for row in results:
			pkg_idMap[row[0]] = int(row[1])
		lastSoftId = int(results[-1][1])
		for row in results:
			softId = int(row[1])
			dependancyListRaw = row[2]
			if dependancyListRaw:
				dependancyListRaw = dependancyListRaw.replace("|",",")
				for dependancyRaw in dependancyListRaw.split(','):
					dependancyRaw = dependancyRaw.partition('(')
					dependancy = dependancyRaw[0]
					dependancy = dependancy.strip()
					if dependancy:
						if dependancy in pkg_idMap:
							dependancyId = pkg_idMap[dependancy.strip()]
						else:
							lastSoftId += 1
							pkg_idMap[dependancy] = lastSoftId
							dependancyId = lastSoftId
							new_pkg_idList = "{},({},{})".format(new_pkg_idList,softId,lastSoftId)
						dependancyIdList = "{},({},{})".format(dependancyIdList,softId,dependancyId)
						count +=1
				if 1000 <= count:
					count = 0
					dependancyIdList = dependancyIdList.replace(',', '', 1)
				
					dependancyIdList = "{}{}".format(depSqlText,dependancyIdList )
					try:
						cursor = conn.cursor()
						cursor.execute(dependancyIdList)
						error = cursor.fetchall()
						cursor.close()
					except Exception as error:
						pass
					dependancyIdList = ''
		if count != 1000 and count:
			dependancyIdList = dependancyIdList.replace(',', '', 1)
			dependancyIdList = "{}{}".format(depSqlText,dependancyIdList )
			try:
				cursor = conn.cursor()
				cursor.execute(dependancyIdList)
				error = cursor.fetchall()
				cursor.close()
			except  Exception as error:
				pass
		new_pkg_idList = new_pkg_idList.replace(',', '', 1)
		new_pkg_idList = "{}{}".format(pkgSqlText,new_pkg_idList )
		try:
			cursor = conn.cursor()	
			cursor.execute(new_pkg_idList)
			error = cursor.fetchall()
		except Exception as error:
			pass

		if error:
			print(error)
		else:
			print ("done")
		conn.close()



setDependancies()
