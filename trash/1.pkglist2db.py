####Sat 14 Jul 2012 06:23:50 PM IST 


from create_temp_table 	import createTempTable
from db_connect 		import DBConnect


def pkgList2DB( content, mainCat, subCat):


	count			= 0
	allCount		= 0
	installedSize 	= 0
	size 			= 0
	descMore		= ""
	moreInfo		= ""
	package 		= None
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

	dbcolumns = (	"Package",
					"Installed_Size",
					"Size",
					"Version",
					"Priority",
					"Section",
					"Maintainer",
					"Homepage",
					"Source",
					"Description",
					"Architecture",
					"Filename",
					"Tag",
					"Depends",
					"Suggests",
					"Recommends",
					"Provides",
					"Replaces",
					"Conflicts",
					"desc_more",
					"more_info",
					"main_category",
					"sub_category"		)


	SQL = "INSERT IGNORE INTO 'software' {0} VALUES ({1}? )".format(dbcolumns[:1], "?, "*(len(dbcolumns[:1])-1))
	SQL = SQL.replace("'","")
	SQL = SQL.replace(",","")


	values = (	package,
				installedSize,
				size,
				version,
				priority,
				section,
				maintainer,
				homepage,
				source,
				description,
				architecture,
				filename,
				tag,
				depends,
				suggests,
				recommends,
				provides,
				replaces,
				conflicts,
				descMore,
				moreInfo,
				mainCat,
				subCat 		)
	
	conn = DBConnect()

#	createTempTable()

	print("Inserting data into table 'software'")##########################################
	
	temp = ""
	tempValues = []

	
	
	for line in content :			#TODO replace everything which are ugly
		if len(line) == 1:
			count += 1
			allCount += 1
			descMore = replaceSpecialChars(descMore)
			moreInfo = replaceSpecialChars(moreInfo)
#			tempValues.append(values[:1])
			installedSize 	= '0'
			size 			= '0'
			descMore		= ""
			moreInfo		= ""
			package 		= None
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
			if 	 key == "Package" 		: package 		= keyText
			elif key == "Installed-Size": installedSize = keyText
			elif key == "Size"			: size			= keyText
			elif key == "Version"		: version		= keyText
			elif key == "Priority"		: priority		= keyText
			elif key == "Section"		: section		= keyText
			elif key == "Maintainer"	: maintainer	= keyText 
			elif key == "Homepage"		: homepage		= keyText
			elif key == "Source"		: source		= keyText
			elif key == "Description"	: description	= keyText
			elif key == "Architecture"	: architecture	= keyText
			elif key == "Filename"		: filename		= keyText
			elif key == "Tag"			: tag			= keyText
			elif key == "Depends"		: depends		= keyText
			elif key == "Suggests"		: suggests		= keyText
			elif key == "Recommends"	: recommends	= keyText
			elif key == "Provides"		: provides		= keyText
			elif key == "Replaces"		: replaces		= keyText
			elif key == "Conflicts"		: conflicts		= keyText
			else:	moreInfo += "{}:{}\n".format( key, keyText)

			values = (	package,
						installedSize,
						size,
						version,
						priority,
						section,
						maintainer,
						homepage,
						source,
						description,
						architecture,
						filename,
						tag,
						depends,
						suggests,
						recommends,
						provides,
						replaces,
						conflicts,
						descMore,
						moreInfo,
						mainCat,
						subCat 		)


		if count == 1:
			count = 0
			conn.executemany(SQL,"fuck")
			print(tempValues)
			tempValues = []
			break
	if count :
			#conn.executemany(SQL,tempValues)
			pass


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
	
