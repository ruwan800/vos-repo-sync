##Wed 12 Sep 2012 01:49:43 AM IST 

from db_connect import DBConnect

def update_pkg_list():
	
	SQL = 	"""
			INSERT INTO 
			software_settings (package,soft_id,new) 
			SELECT package,id,'YES'
			FROM software 
			WHERE 
			package NOT IN (SELECT package FROM software_settings)
			"""

	conn = DBConnect()
	conn.execute(SQL)
	SQL = "SELECT COUNT(*) FROM software_settings WHERE new = 'YES'"
	result = conn.execute(SQL)
	print(str(result) + " packages newly added.")
	conn.close()
