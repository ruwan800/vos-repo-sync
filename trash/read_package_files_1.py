from glob import glob
import gzip
import bz2
from config.repo import repo
from pkglist2db import pkgList2DB
from get_packages import deleteListPackages


def readPackageFiles():
	
	print("readPackageFiles.py started")########################################
	tempDir	= repo.repoDir
	packageFiles = glob(tempDir+"/*")
	for packageFile in packageFiles:
		print( "Reading "+ packageFile) ########################################
		cat = packageFile.split("__")
		if 3 <= len(cat):
			mainCategory = cat[0]
			subCategory  = cat[1]
			Filetype = cat[2].split(".")[-1]
			if Filetype is "gz":
				content = gzip.open( packageFile, 'r')
			elif Filetype is "bz2":
				content = bz2.BZ2File( packageFile, 'r')
			pkgList2DB(content,mainCategory,subCategory)
			content.close()
		else:
			print( "Error reading "+ packageFile) ##############################
	if repo.externalLink:
		deleteListPackages()
	print("readPackageFiles.py done")###########################################

