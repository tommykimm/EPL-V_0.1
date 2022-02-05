import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="12345",
  database="practice"
)

mycursor = mydb.cursor()
sql = "DELETE FROM practice.MyUsers"
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")