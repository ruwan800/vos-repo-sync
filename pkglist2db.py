####Sat 14 Jul 2012 06:23:50 PM IST 


from create_temp_table 	import createTempTable
from db_connect 		import DBConnect


def pkgList2DB( content, mainCat, subCat):


	count			= 0
	allCount		= 0
	SQLTempText		= ""
	descMore		= ""
	moreInfo		= ""
	package 		= None
	installedSize 	= 0
	size 			= 0
	version			= None
	priority		= None
	section			= None
	maintainer		= None
	homepage		= None
	source			= None
	description		= None
	architecture	= None
	filename		= None
	tag				= None
	depends			= None
	suggests		= None
	recommends		= None
	provides		= None
	replaces		= None
	conflicts		= None
	SQLText = "INSERT IGNORE INTO software "

	columns = {
				"Package"		: package,
				"Installed-Size": installedSize,
				"Size"			: size,
				"Version"		: version,
				"Priority"		: priority,
				"Section"		: section,
				"Maintainer"	: maintainer, 
				"Homepage"		: homepage,
				"Source"		: source,
				"Description"	: description,
				"Architecture"	: architecture,
				"Filename"		: filename,
				"Tag"			: tag,
				"Depends"		: depends,
				"Suggests"		: suggests,
				"Recommends"	: recommends,
				"Provides"		: provides,
				"Replaces"		: replaces,
				"Conflicts"		: conflicts,
			  }
	
	conn = DBConnect()

#	createTempTable()

	print("Inserting data into table 'software'")##########################################
	
	temp = ""
	for key in columns:
		temp = "{}, {}".format( temp, key)
	SQLText = "{}( desc_more, more_info{},main_category, sub_category ) VALUES ".format( SQLText,temp)
	SQLText = SQLText.replace("Installed-Size","Installed_size") 
	
	
	for line in content :			#TODO replace everything which are ugly
		if len(line) == 1:
			count += 1
			allCount += 1
			descMore = replaceSpecialChars(descMore)
			moreInfo = replaceSpecialChars(moreInfo)
			tempText = ""
			for key in columns:
				tempText = "{}, '{}'".format( tempText, columns[key])
			SQLTempText  = "{}, ('{}', '{}'{}, '{}','{}')".format( SQLTempText, descMore, moreInfo, tempText, mainCat, subCat )
			for key in columns:
				columns[key] = ""
			descMore		 = ""
			moreInfo		 = ""
			
		elif line[0] is " ":
			if len( line) == 4:
				descMore += "\n"
			else:
				descMore += line[1:]
		else:
			line = line.strip()
			line = line.partition(":")
			key  = line[0]
			keyText  = line[2]
			if key in columns:
				columns[key] = replaceSpecialChars(keyText).strip()
			else:
				moreInfo += "{}:{}\n".format( key, keyText)

		if count == 100:
			count = 0
			SQLTempText = "{} {}".format( SQLText, SQLTempText[1:])
			conn.execute(SQLTempText)
			SQLTempText = ""
	if count != 100 and count !=0:
		SQLTempText = "{} {}".format( SQLText, SQLTempText[1:])
		conn.execute(SQLTempText)


	print(str(allCount)+ " items inserted/updated")############################################
#	print("Updating table 'software'")##########################################
#	SQL = "CALL sw_list_update('{}','{}')".format)(mainCat, subCat)# TODO execute INTERNAL SQL SP:
#	result = conn.execute(SQL)

	
	conn.close()
#	print(result+ " items updated in table 'software'")#########################


def replaceSpecialChars(text):
	specialChars = { "\"":"&quot;", "\'":"&#039;", "<":"&lt;", ">":"&gt;"}
	if text:
		text = text.replace("\t","")
		text = text.replace("&","&amp;")
		text = text.replace("\"","&quot;")
		text = text.replace("\'","&#039;")
		text = text.replace("<","&lt;")
		text = text.replace(">","&gt;")
		text = text.replace("\n","</br>")
	return text
	
