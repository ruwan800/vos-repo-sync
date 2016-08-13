from glob import glob
import gzip
import bz2
from config.repo import repo
from pkglist2db import pkgList2DB
from get_packages import deleteListPackages


def readPackageFiles():
	
	print("Reading package-list-files")#########################################
	tempDir	= repo.tempDir
	bPrefix = repo.binaryPrefix

	count = 0
	for mainDir in glob(tempDir+"/dists/*"):
		mainCat = mainDir[len(tempDir)+7:]
		for ubuntuVersionName in repo.ubuntuVersions:
			if ubuntuVersionName in mainCat:
				for subDir in glob(mainDir+"/*"):
					subCat = subDir[len(mainDir)+1:]
					pkgFiles = glob( subDir+ "/"+ bPrefix+ "/*")
					if pkgFiles:
						for fileDir in pkgFiles:
							fileName = fileDir.rpartition( "/")[2]
							if fileName == "Packages.gz":
								print( "Reading Package-file     "+ fileDir) ###
								content = gzip.open( fileDir, 'r')
								pkgList2DB(content,mainCat,subCat)
								content.close()
								count += 1
								break
							elif fileName == "Packages.bz2":
								print( "Reading Package-file     "+ fileDir) ###
								content = bz2.BZ2File( fileDir, 'r')
								pkgList2DB(content,mainCat,subCat)
								content.close()
								count += 1
								break
							else:
								print ("no Package-file found in "+ subDir)
					else:
						print ("no Package-file found in "+ subDir)


	print("finished reading "+ str( count)+ " package-list-files")##############
	
	return count != 0

