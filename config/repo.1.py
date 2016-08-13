import ConfigParser


class repo:

	"""Configurations for repository"""

	def __init__(self):

		Config = ConfigParser.ConfigParser()
		Config.read("repository.ini")
		if Config.get('Default', 'repositoryinuse')== 'local' :
			self.externalLink	= None
			self.repoDir		= Config.get('Default', 'localrepository')
			if self.repoDir[-1] == '/':
				self.repoDir = self.repoDir[:-1]
		else :
			self.repoDir 		= None
			self.externalLink	= Config.get('Default', 'externalrepository')
			if self.externalLink[-1] == '/':
				self.externalLink = self.externalLink[:-1]
		self.tempDir 			= Config.get('Default', 'tempdirectory')
		if self.tempDir[-1] == '/':
			self.tempDir = self.tempDir[:-1]
		self.ubuntuVersions		= [ x.split() for x in Config.get('Default', 'ubuntuversions').split(',') ]
		self.mainCategories		= [ x.split() for x in Config.get('Default', 'maincategories').split(',') ]
		self.subCategories		= [ x.split() for x in Config.get('Default', 'subcategories').split(',') ]
		self.fileNames			= [ x.split() for x in Config.get('Default', 'filenames').split(',') ]
		self.binaryPrefix 		= Config.get('Default', 'binaryprefix')

repo = repo()



