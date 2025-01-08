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
#cursor.execute("CREATE DATABASE little_lemon_db")
cursor.execute("USE little_lemon_db")

#MenuItems table
create_menuitem_table = """CREATE TABLE MenuItems (
ItemID INT AUTO_INCREMENT,
Name VARCHAR(200),
Type VARCHAR(100),
Price INT,
PRIMARY KEY (ItemID)
);"""

create_menu_table = """CREATE TABLE Menus (
MenuID INT,
ItemID INT,
Cuisine VARCHAR(100),
PRIMARY KEY (MenuID,ItemID)
);"""

create_booking_table = """CREATE TABLE Bookings (
BookingID INT AUTO_INCREMENT,
TableNo INT,
GuestFirstName VARCHAR(100) NOT NULL,
GuestLastName VARCHAR(100) NOT NULL,
BookingSlot TIME NOT NULL,
EmployeeID INT,
PRIMARY KEY (BookingID)
);"""


create_orders_table = """CREATE TABLE Orders (
OrderID INT,
TableNo INT,
MenuID INT,
BookingID INT,
BillAmount INT,
Quantity INT,
PRIMARY KEY (OrderID,TableNo)
);"""


create_employees_table = """CREATE TABLE Employees (
EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR (255),
Role VARCHAR (100),
Address VARCHAR (255),
Contact_Number INT,
Email VARCHAR (255),
Annual_Salary VARCHAR (100)
);"""



# Create MenuItems table
cursor.execute(create_menuitem_table)

# Create Menu table
cursor.execute(create_menu_table)

# Create Bookings table
cursor.execute(create_booking_table)

# Create Orders table
cursor.execute(create_orders_table)

# Create Employees table
cursor.execute(create_employees_table)





print("Connection successful!")
