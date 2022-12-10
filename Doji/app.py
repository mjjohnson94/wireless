from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)

@app.route('/')

def landingPage():
        return render_template('landingPage.html')


@app.route('/', methods=['POST'])
def registerUser():

        firstName = request.form['firstName']
        secondName = request.form['secondName']
        eMail = request.form['eMail']
        phoneNumber = request.form['phoneNumber']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']

        registrationForm = [firstName, secondName, 
                           eMail, phoneNumber, 
                           password, confirmPassword]

        return render_template('index.html', text=firstName)

