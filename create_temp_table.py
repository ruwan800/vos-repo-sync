

from db_connect import DBConnect


def createTempTable():

#		print("Creating temporary table")#######################################
		
		conn = DBConnect()

#		SQL = "DROP TABLE IF EXISTS sc_temp"
#		conn.execute(SQL)
							
#		SQL =	"""		
#				CREATE TABLE sc_temp (
#				  `package`			varchar(70)	NOT NULL,
#				  `installed_size`	int(11)					DEFAULT NULL,
#				  `size`			int(11)					DEFAULT NULL,
#				  `version`			text,
#				  `priority`		text,
#				  `section`			text,
#				  `maintainer`		text,
#				  `homepage`		text,
#				  `source`			text,
#				  `description`		text,
#				  `architecture`	text,
#				  `filename`		text,
#				  `tag`				text,
#				  `depends`			text,
#				  `suggests`		text,
#				  `recommends`		text,
#				  `desc_more`		text,
#				  `provides`		text,
#				  `replaces`		text,
#				  `conflicts`		text,
#				  `more_info`		text,
#				  `main_category`	text,
#				  `sub_category`	text,
#				  KEY `package` (`package`) USING BTREE
#				) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
#				"""
		
#		conn.execute(SQL)
		
		conn.close()


