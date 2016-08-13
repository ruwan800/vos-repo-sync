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
			results = None
		if results:
			results = self.modResult(results)
		return results
	
	def close(self):
		self.conn.close()

	def executemany(self,SQL,ourList):
		try:
			cursor = self.conn.cursor()
			cursor.executemany(SQL,ourList)
			self.conn.commit()
#			results = cursor.fetchall()
			cursor.close()
#			print("SQL::success")		########################################
		except  Exception as error:
			print("SQL::error")			########################################
			print(error)				########################################
			print(SQL[:10000])			########################################

	def modResult(self,result):
		if not result:
			result = None
		elif len(result[0]) == 1:
			if len(result) == 1:
				result = str(result[0][0])
			else:
				temp = []
				for item in result:
					temp.append(str(item[0]))
				result = temp
		elif len(result) == 1:
			temp = []
			for item in result[0]:
				temp.append(str(item))
			result = temp
		else:
			temp1 = []
			for i in result:
				temp2 = []
				for j in i:
					temp2.append(str(j))
				temp1.append(temp2)
			result = temp1
		return result


#DBConnect = DBConnect()
