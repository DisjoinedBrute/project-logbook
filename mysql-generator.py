import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='sid@191203'
)

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE logbook')
mycursor.execute("USE logbook")
mycursor.execute('CREATE TABLE users (teacherid VARCHAR(30), username  VARCHAR(30) , password VARCHAR(30))')
mycursor.execute('CREATE TABLE 11a (teacherid VARCHAR(25), date  VARCHAR(25) , subject VARCHAR(25), chaps TEXT) ')
mycursor.execute('CREATE TABLE 11b (teacherid VARCHAR(25), date  VARCHAR(25) , subject VARCHAR(25), chaps TEXT) ')
mycursor.execute('CREATE TABLE 11c (teacherid VARCHAR(25), date  VARCHAR(25) , subject VARCHAR(25), chaps TEXT) ')

sql = 'INSERT INTO users (teacherid, username , password) VALUES (%s, %s , %s)'
val = [
    ('B/0001', 'Shobha' , 'shobha1234'),
    ('B/0002', 'Vasudha' , 'vasudha1234'),
    ('B/0003', 'Sai' , 'sai1234'),
    ('B/0004', 'Rajeev' , 'rajeev1234'),
    ('B/0005', 'Siddharth' , 'siddharth1234').
]

mycursor.executemany(sql, val)
mydb.commit()
