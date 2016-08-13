####  Fri 13 Jul 2012 01:03:27 AM IST 

from db_connect import DBConnect



def setTags():
		
		count = 0
		tagValueList = ''
		pkgSQLText = "INSERT DELAYED INTO tag_list ( soft_id,tag_main,tag_sub ) VALUES "


		print("Setting-up tags for packages")###################################

		conn = DBConnect()

		SQL = "SELECT t1.soft_id, t2.tag FROM software_settings AS t1, software AS t2 WHERE t1.package = t2.package"
		results = conn.execute(SQL)

		for row in results:
			softId = int(row[0])
			tagListRaw = row[1]
			if tagListRaw and tagListRaw != 'None':
				tagListRaw = tagListRaw.replace("{","")
				tagListRaw = tagListRaw.replace("}","")
				for tagRaw in tagListRaw.split(','):
					tagRaw = tagRaw.partition('::')
					if tagRaw[1]:
						tagMain = tagRaw[0].strip()
						tagSub = tagRaw[2].strip()
					else:
						tagSub = tagRaw[0].strip()
					tagValueList = "{},({},'{}','{}')".format(tagValueList,softId,tagMain,tagSub)
					count +=1
				if 1000 <= count:
					count = 0
					tagValueList = tagValueList.replace(',', '', 1)
					SQL = "{}{}".format(pkgSQLText,tagValueList)
					conn.execute(SQL)
					tagValueList = ''
		if count != 1000 and count:
			tagValueList = tagValueList.replace(',', '', 1)
			SQL = "{}{}".format(pkgSQLText,tagValueList)
			conn.execute(SQL)
		SQL = "SELECT COUNT(*) FROM tag_list "
		result = conn.execute(SQL)
		conn.close()
		print(result+ " tags were set")#########################################


