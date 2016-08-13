import urllib2
import shutil
import os
from config.repo import repo

def getListPackages():

	"""download Packages.gz files from a remote directory"""

	filenames			= repo.fileNames
	repository			= repo.externalLink
	tempDir				= repo.repoDir
	ubuntuVersionName	= repo.ubuntuVersionName
	mainCategories 		= repo.mainCategories
	subCategories 		= repo.subCategories
	binaryPrefix		= repo.binaryPrefix

	if repository:
		if not os.path.isdir(tempDir):
			os.mkdir(tempDir)

		for mainCategory in mainCategories:
			for subCategory in subCategories:
				for filename in fileNames:
					if mainCategory:
						link="{}/dists/{}-{}/{}/{}".format(repository,ubuntuVersionName,
															mainCategory,subCategory,binaryPrefix)
					else:
						link = "{}/dists/{}/{}/{}".format(repository,ubuntuVersionName,subCategory,binaryPrefix)
					link = "{}/{}".format(link,filename)
					try:
						packageFile = urllib2.urlopen( link)
					except :
						packageFile = None
						print (link+" not found")
					if packageFile :
						filename = "{}/{}__{}__{}".format(tempDir,mainCategory,subCategory,filename)
						output = open( filename, 'wb')
						output.write(packageFile.read())
						output.close()	
						break


def deleteListPackages():
	tempDir = repo.repoDir
	shutil.rmtree(tempDir)


