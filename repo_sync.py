from set_dependancies 	import setDependancies
from read_package_files	import readPackageFiles
from drop_tables 		import dropTables
from get_packages 		import *
from set_tags 			import setTags
from update_pkg_list	import update_pkg_list

##putting data into db:
	
filesAvailable = getListPackages()
if filesAvailable:
	dropTables()
	filesAvailable = readPackageFiles()
	if filesAvailable:
		#update_pkg_list()
		setDependancies()
		#setTags()
		print("DONE :)")
	else:
		print("No package files found :(\n END")

#deleteListPackages()

