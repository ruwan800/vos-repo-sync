import urllib2
import shutil
import os
from config.repo import repo

def getListPackages():

	###TODO set to automatically resolve directories

	"""Downloading Packages.gz files from a remote directory"""

	fileNames			= repo.fileNames
	repository			= repo.externalLink
	repoDir				= repo.repoDir
	tempDir				= repo.tempDir
	ubuntuVersions		= repo.ubuntuVersions
	mainCategories 		= repo.mainCategories
	subCategories 		= repo.subCategories
	binaryPrefix		= repo.binaryPrefix
	count = 0

	if not os.path.isdir(tempDir):
		os.mkdir(tempDir)
	if repository:


		print("Downloading package-list-files")#################################
		for ubuntuVersionName in ubuntuVersions:
			for mainCategory in mainCategories:
				for subCategory in subCategories:
					for filename in fileNames:
						if mainCategory:
							link="/dists/{}-{}/{}/{}".format(ubuntuVersionName,
																mainCategory,subCategory,binaryPrefix)
						else:
							link = "/dists/{}/{}/{}".format(ubuntuVersionName,subCategory,binaryPrefix)
						linkTemp = "{}{}/{}".format(repository,link,filename)
						print("Downloading: " + linkTemp)##########################
						try:
							packageFile = urllib2.urlopen( linkTemp)
						except :
							packageFile = None
							print (" Not found: " + linkTemp)
						if packageFile :
							fileDir = "{}{}".format(tempDir,link)
							fileLink = "{}{}/{}".format(tempDir,link,filename)
							if not os.path.isdir(fileDir):
								os.makedirs(fileDir)
							output = open( fileLink, 'wb+')
							output.write(packageFile.read())
							output.close()
							count += 1
							break
		if count:
			print("Download complete. "+ str(count)+ "files downloaded")########
		else:
			print("Failed to download package files :(\n END")##################
	else:
		if not os.path.isdir(repoDir):
			print("Local repository not found. :(\n END")##################
		else:
			count = 1
			if os.path.isdir(tempDir):
				deleteListPackages()
#				os.mkdir("{}/dists".format(tempDir))
				shutil.copytree("{}/dists".format(repoDir), "{}/dists".format(tempDir))
				shutil.copystat("{}/dists".format(repoDir), "{}/dists".format(tempDir))
				
			
	
	return count != 0

def deleteListPackages():
	tempDir = repo.tempDir
	shutil.rmtree(tempDir, 'ignore_errors' )


