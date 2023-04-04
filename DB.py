import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ashu"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")