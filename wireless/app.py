from flask import Flask, render_template, request
from pandas.core.base import DataError
import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr

app = Flask(__name__)

@app.route('/')

def landingPage():

        return render_template('landingPage.html')

