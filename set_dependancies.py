####Wed 11 Jul 2012 08:31:01 PM IST 

from db_connect import DBConnect



def setDependancies():
		

		dependancyIdList = ''
		depSQLText = "INSERT DELAYED INTO dependancies ( dependant, dependancy ) VALUES "
#		pkgSQLText = "INSERT INTO software_settings ( package , soft_id ) VALUES "#TODO set other options
		count = 0
		
		print("Setting-up dependancies for packages")###########################

		conn = DBConnect()

		SQL = 	" SELECT package, depends  FROM software "
		results = conn.execute(SQL)
		for row in results:
			package = row[0]
			dependancyListRaw = row[1]
			if dependancyListRaw:
				dependancyListRaw = dependancyListRaw.replace("|",",")
				for dependancyRaw in dependancyListRaw.split(','):
					dependancyRaw = dependancyRaw.partition('(')
					dependancy = dependancyRaw[0]
					dependancy = dependancy.strip()
					if dependancy:
						dependancyIdList = "{},('{}','{}')".format(dependancyIdList,package,dependancy)
						count +=1
				if 1000 <= count:
					count = 0
					dependancyIdList = dependancyIdList.replace(',', '', 1)
					dependancyIdList = "{}{}".format(depSQLText,dependancyIdList )
					conn.execute(dependancyIdList)
					dependancyIdList = ''
		if count :
			dependancyIdList = dependancyIdList[1:]
			dependancyIdList = "{}{}".format(depSQLText,dependancyIdList )
			conn.execute(dependancyIdList)
		
		SQL = "SELECT COUNT(*) FROM dependancies "
		result = conn.execute(SQL)
		conn.close()
		print (result+ " different dependancies have been set")#################

