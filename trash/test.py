from db_connect import DBConnect


hello = DBConnect()
SQL = "SELECT 0 FROM software WHERE soft_id = 1234;"
results = hello.execute(SQL)
print(results)

