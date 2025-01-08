# Import MySQL Connector/Python 
from dotenv import load_dotenv
import os
import mysql.connector as connector

# Load environment variables from the .env file
load_dotenv()

# Get the variables from the environment
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# Connect to the database
connection = connector.connect(user=db_user, password=db_password)

# Create a cursor object using the cursor() method
cursor = connection.cursor()
cursor.execute("CREATE DATABASE little_lemon_db")
cursor.execute("USE little_lemon_db")


print("Connection successful!")
