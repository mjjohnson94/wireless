from flask import Flask, render_template, request
import pandas as pd
import psycopg2

app = Flask(__name__)

@app.route('/')

def landingPage():
        return render_template('landingPage.html')


@app.route('/', methods=['POST'])
def registerUser():

        firstName = request.form['firstName']
        secondName = request.form['lastName']
        eMail = request.form['eMail']
        phoneNumber = request.form['phoneNumber']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']

        ID = 1

        # Establish connection to PostgreSQL database 

        conn = psycopg2.connect(
        host="localhost",
        database="pythontestdb",
        user="postgres",
        password="AAA009wn73ed")

        cur = conn.cursor()

        cur.execute("INSERT INTO registered_users(ID, FIRST_NAME, LAST_NAME, EMAIL_ADDRESS, PHONE_NUMBER, PASSWORD) VALUES(%s, %s, %s, %s, %s, %s)",
        (ID, firstName, secondName, eMail, phoneNumber, password))

        conn.commit()
        cur.close()
        conn.close()

        return render_template('index.html')
