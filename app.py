import os
import mysql.connector
from flask import Flask, render_template, request, session

app = Flask(__name__)

# Database connection
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
    database='logbook'
)

mycursor = mydb.cursor()


# Runs when the user goes to the URL
@app.route('/')
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('dashboard.html')


# When form sends back data
@app.route('/auth', methods=['POST'])
def login():
    mycursor.execute(
        f"SELECT * FROM users WHERE username = '{request.form['username']}' AND password = '{request.form['pass']}'")
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        session['logged_in'] = True
        return render_template('dashboard.html')
    else:
        return index()


# When user tries to access dashboard
@app.route('/dashboard')
def viewdash():
    if session.get('logged_in'):
        return render_template('dashboard.html')
    else:
        return index()


@app.route('/submit', methods=['POST'])
def submit():
    mycursor.execute(
        f"INSERT INTO `{request.form['class_section']}` (teacherid, date, subject, chaps) VALUES ('{request.form['teacherid']}', '{request.form['date']}' , '{request.form['subject']}', '{request.form['chapsdone']}')")
    mydb.commit()
    return render_template('login.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', port=8080)  # Basically runs the website on localhost:8080
