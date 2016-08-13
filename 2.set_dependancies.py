####Wed 11 Jul 2012 08:31:01 PM IST 

from db_connect import DBConnect



def setDependancies():

		dependancyList = []
		SQL = "INSERT DELAYED INTO 'dependancies' ( main_soft_id, dep_soft_id ) VALUES (?, ? )"
		count = 0
		
		print("Setting-up dependancies for packages")###########################

		conn = DBConnect()

		SQLget = 	" SELECT package, depends  FROM software "
		results = conn.execute(SQLget)

		for row in results:
			package = row[1]
			dependancyListRaw = row[1]
			if dependancyListRaw:
				dependancyListRaw = dependancyListRaw.replace("|",",")
				for dependancyRaw in dependancyListRaw.split(','):
					dependancyRaw = dependancyRaw.partition('(')
					dependancy = dependancyRaw[0]
					dependancy = dependancy.strip()
					if dependancy:
						dependancyList.append((package,dependancy)) 
						count +=1
				if 1000 <= count:
					count = 0
					conn.executemany(SQL,dependancyList)
					dependancyList = []
		if count :
			conn.executemany(SQL,dependancyList)
		
		SQL = "SELECT COUNT(*) FROM dependancies "
		result = conn.execute(SQL)
		conn.close()
		print (result+ " different dependancies have been set")#################

