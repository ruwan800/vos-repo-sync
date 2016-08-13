


class repo:

	"""Configurations for repository"""

	def __init__(self):

		##if externalLink available it will used instead of repoDir
		##if not using externalLink set it to None
		##externalLink example("http://mirrors.us.kernel.org/ubuntu")
		##repoDir example("/var/www/repo")
		self.externalLink 		= None#"http://mirrors.us.kernel.org/ubuntu" 	#TODO strip last / if exists
		self.repoDir 			=  "/var/www/repo" #None						#TODO strip last / if exists 
		self.tempDir 			= "/tmp/repo"									#TODO strip last / if exists
		self.ubuntuVersions		= ["maverick"]
		self.mainCategories 	= [ None, "updates", "security", "proposed", "backports"]
		self.subCategories 		= [ "main", "multiverse", "restricted", "universe"]
		self.binaryPrefix 		= "binary-i386"
		self.fileNames			= [ "Packages.gz", "Packages.bz2"]

repo = repo()



