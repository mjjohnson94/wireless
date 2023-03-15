# Import dependencies 

from aem import con
from flask import Flask, render_template, request
from numpy import record
import pandas as pd
import psycopg2

# Initialize app class

app = Flask(__name__)


# Crate default app route (landing page)
@app.route('/')

# Create function to load landingPage.html DOM, use render_template function 
def landingPage():
        return render_template('landingPage.html')


# Create function to load registerUser.html DOM for new users 
# Use POST method to send data from the client-side to server-side 
@app.route('/registerUser', methods=['POST'])
def registerUser():

        # Return ther registerUser.html DOM
        return render_template('registerUser.html')
        

# Create function to handle new user submitting a registration form 
# Use POST method to send data from the client-side to server-side 
# Specifically, the registeration data will be inputted in the HTML document by the user (client-side) & sent to a PostgreSQL database (server-side)
@app.route('/submitUser', methods=['POST'])
def submitUser():


        ## Create an object for each form element that will be inserted into the database
        # Use the request.form.get function to request data from HTML element 
        ID = 0
        email = request.form.get('email_Register')
        username = request.form.get('username_Register')
        password = request.form.get('password_Register')

        # Establish connection to PostgreSQL database 

        conn = psycopg2.connect(
        host="localhost",
        database="pythontestdb",
        user="postgres",
        password="AAA009wn73ed")

        # Create instance of cursor class, which enables Python code to execute PostgreSQL commands in a database session
        cur = conn.cursor()

        # Create PosgreSQL INSERT query, use the objects created above to form the data for the record 
        query = """ INSERT INTO REGISTERED_USERS (ID, USERNAME, EMAIL_ADDRESS, PASSWORD) VALUES (%s, %s, %s, %s) """
        record = (ID, username, email, password)

        # Execute the query which will insert the record into the relevant database table 
        cur.execute(query, record)      

        # Commit command 
        conn.commit()
        
        # Return new DOM named userHome.html
        return render_template('userHome.html', username)


## Create function to handle existing user login 
# Use POST method to send data from the client-side to server-side 
@app.route('/logIn', methods=['POST'])
def logIn():

        # Create an object for each form element that will be used to handle login request 
        # Use the request.form.get function to request data from HTML element 
        eMail = request.form['Email']
        password = request.form['PassW']

        # Establish connection to PostgreSQL database 

        conn = psycopg2.connect(
        host="localhost",
        database="pythontestdb",
        user="postgres",
        password="AAA009wn73ed")

        # Create instance of cursor class, which enables Python code to execute PostgreSQL commands in a database session
        cur = conn.cursor()

         # Create PosgreSQL SELECT query, use the objects created above to form the data for the record 
        query = 'SELECT * FROM registered_users WHERE email_address LIKE %s AND password LIKE %s' 
        record = (eMail, password)

        # Execute the query which will insert the record into the relevant database table 
        cur.execute(query, record)  
        
        # Use the fetchall command to return all database records that match the criteria set in the query object
        recordValidation = cur.fetchall()

        # Apply logic of if 1 record exists, the email & password are correct for the user so they proceed to login
        # The email/password columns in the PostgreSQL database accepts unique values only, meaning there should only be one instance of each email address & password combination
        if len(recordValidation) > 0:
                return render_template('userHome.html')

        # If there are no records,  then the user does not have valid login credentials and is thereby directed to the login fail HTML DOM
        else:
                return render_template('logInFail.html')





