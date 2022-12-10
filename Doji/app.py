from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)

@app.route('/')

def landingPage():
        return render_template('landingPage.html')


@app.route('/', methods=['POST'])
def registerUser():

        firstName = request.form['firstName']
        secondName = request.form['lastName']
        
     

        return render_template('index.html', text=firstName, x=secondName)

