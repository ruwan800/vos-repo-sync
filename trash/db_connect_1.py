import MySQLdb
from config.db import DB


class DBConnect:
	
	def __init__(self):
		DB_NAME = DB.NAME
		DB_HOST = DB.HOST
		DB_USER = DB.USER
		DB_PASS = DB.PASS
		self.conn = MySQLdb.Connection(db=DB_NAME, host=DB_HOST, user=DB_USER,passwd=DB_PASS)

	def execute(self,SQL):
		try:
			cursor = self.conn.cursor()
			cursor.execute(SQL)
			results = cursor.fetchall()
			cursor.close()
#			print("SQL::success")		########################################
		except  Exception as error:
			print("SQL::error")			########################################
			print(error)				########################################
			print(SQL)					########################################
			results = False
		return results
	
	def close(self):
		self.conn.close()

#DBConnect = DBConnect()


