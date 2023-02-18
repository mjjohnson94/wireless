from flask import Flask, render_template, request
import pandas as pd
import psycopg2

app = Flask(__name__)

@app.route('/')

def landingPage():
        return render_template('landingPage.html')


@app.route('/registerUser', methods=['POST'])
def registerUser():

        return render_template('registerUser.html')
        

@app.route('/submitUser', methods=['POST'])
def submitUser():
        
        return render_template('index.html')


@app.route('/logIn', methods=['POST'])
def logIn():

        eMail = request.form['Email']
        password = request.form['PassW']

        conn = psycopg2.connect(
        host="localhost",
        database="pythontestdb",
        user="postgres",
        password="AAA009wn73ed")

        cur = conn.cursor()

        cur.execute('SELECT * FROM registered_users WHERE email_address LIKE %s AND password LIKE %s', (eMail, password,))
        x = cur.fetchall()

        if len(x) > 0:
                return render_template('loggedIn.html')
        else:
                return render_template('logInFail.html')





