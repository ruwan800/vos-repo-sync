#### Fri 13 Jul 2012 01:14:45 AM IST 

from db_connect import DBConnect

def dropTables():

		print("Deleting some old tables")#######################################
		
		conn = DBConnect()
		
		SQL = " DROP TABLE IF EXISTS `dependancies` ; "
		conn.execute(SQL)
	
#		SQL = " DROP TABLE IF EXISTS `tag_list` ; "
#		conn.execute(SQL)

		SQL = " DROP TABLE IF EXISTS `software` ; "
		conn.execute(SQL)

		SQL = """
				CREATE TABLE IF NOT EXISTS `dependancies` (
	  			`id` 			int(10) 		NOT NULL 	AUTO_INCREMENT,
	  			`dependant` 	varchar(70) 	NOT NULL,
	  			`dependancy` 	varchar(70) 	NOT NULL,
				 PRIMARY KEY (`id`)
				) ENGINE=MyISAM  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ;	
			  """
		conn.execute(SQL)

#		SQL = """
#				CREATE TABLE IF NOT EXISTS `tag_list` (
#	  			`tag_id` 			int(10) 	NOT NULL 	AUTO_INCREMENT,
#	  			`soft_id` 		int(10) 	NOT NULL,
#	  			`tag_main` 		varchar(30),
#	  			`tag_sub` 		varchar(30),
#	  			PRIMARY KEY (`tag_id`)
#				) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ;
#			  """
#		conn.execute(SQL)


		SQL = """
				CREATE TABLE IF NOT EXISTS `software` (
				  `package`			varchar(70)	NOT NULL,
				  `id`				int(11)		NOT NULL	AUTO_INCREMENT,
				  `installed_size`	varchar(70)				DEFAULT NULL,
				  `size`			varchar(70)				DEFAULT NULL,
				  `date`			int(8)					DEFAULT NULL,
				  `version`			text,
				  `priority`		text,
				  `section`			text,
				  `maintainer`		text,
				  `homepage`		text,
				  `source`			text,
				  `description`		text,
				  `architecture`	text,
				  `filename`		text,
				  `tag`				text,
				  `depends`			text,
				  `suggests`		text,
				  `recommends`		text,
				  `desc_more`		text,
				  `provides`		text,
				  `replaces`		text,
				  `conflicts`		text,
				  `more_info`		text,
				  `main_category`	varchar(70),
				  `sub_category`	varchar(70),
				  PRIMARY KEY (`id`),
				  UNIQUE KEY `package` (`package`)
				) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;
			  """
		conn.execute(SQL)


#		SQL = 	" UPDATE software_settings SET new = 'NO' "
#		conn.execute(SQL)


		conn.close()
