import mysql.connector


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="akash",
  password="Akash@1234",
  database = "akash",
  auth_plugin='mysql_native_password'
)
# print(mydb)
