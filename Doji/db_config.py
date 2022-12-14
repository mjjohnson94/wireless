## Import dependencies - pyscopg2 is a Python-PostgreSQL database adapter 

import psycopg2

# Establish connection to PostgreSQL database 

conn = psycopg2.connect(
    host="localhost",
    database="pythontestdb",
    user="postgres",
    password="AAA009wn73ed")

conn.autocommit = True

cursor = conn.cursor()

# SQL command to CREATE TABLE, assigned to sqlQuery variable

sqlQuery = '''CREATE TABLE registered_users (
          ID INT PRIMARY KEY NOT NULL,
          FIRST_NAME CHAR(500),
          LAST_NAME CHAR(500),
          EMAIL_ADDRESS VARCHAR,
          PHONE_NUMBER INT,
          PASSWORD VARCHAR)'''

# Execute the database operation, the SQL command can be written within the brackets of the cursor.execute method or assigned to a variable 

cursor.execute(sqlQuery)

# Close the cursor once the command has been executed and the connection is no longer required for that specific task 

cursor.close()

# Close the connection once the command has been executed and the connection is no longer required for that specific task

conn.close()