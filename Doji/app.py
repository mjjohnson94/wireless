from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)

@app.route('/')

def landingPage():
        return render_template('landingPage.html')

