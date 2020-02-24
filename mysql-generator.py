import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='password'
)

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE logbook')
mycursor.execute("USE logbook")
mycursor.execute('CREATE TABLE users (teacherid VARCHAR(30), username  VARCHAR(30) , password VARCHAR(30))')
mycursor.execute('CREATE TABLE 11a (teacherid VARCHAR(25), date  VARCHAR(25) , subject VARCHAR(25), chaps TEXT) ')
mycursor.execute('CREATE TABLE 11b (teacherid VARCHAR(25), date  VARCHAR(25) , subject VARCHAR(25), chaps TEXT) ')
mycursor.execute('CREATE TABLE 11c (teacherid VARCHAR(25), date  VARCHAR(25) , subject VARCHAR(25), chaps TEXT) ')

sql = 'INSERT INTO users (teacherid, username , password) VALUES (%s, %s , %s)'
val = ('teacherid', 'username' , 'password')
mycursor.execute(sql, val)
mydb.commit()
