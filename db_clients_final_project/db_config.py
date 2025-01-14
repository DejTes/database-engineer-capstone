from mysql.connector import pooling, Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Database configuration from .env
dbconfig = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_DATABASE"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

try:
    # Step 1: Create a connection pool
    pool_a = pooling.MySQLConnectionPool(pool_name="pool_a", pool_size=2, **dbconfig)
    print("Connection pool created successfully.")
    
    # Step 2: Obtain a connection from the pool
    connection = pool_a.get_connection()
    if connection.is_connected():
        print("Successfully obtained a connection from the pool.")

    # Step 3: Create a cursor object
    cursor = connection.cursor()
    print("Cursor object created successfully.")

    # Task 1: Test connection by executing a query
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("Available tables:", tables)

    # Task 2: Implement PeakHours stored procedure
    peak_hours_query = """
    CREATE PROCEDURE PeakHours()
    BEGIN
        SELECT 
            HOUR(BookingSlot) AS BookingHour, 
            COUNT(*) AS BookingCount
        FROM Bookings
        GROUP BY BookingHour
        ORDER BY BookingCount DESC;
    END;
    """
    cursor.execute("DROP PROCEDURE IF EXISTS PeakHours;")
    cursor.execute(peak_hours_query)
    print("Stored procedure PeakHours created.")

    # Run PeakHours procedure
    cursor.callproc("PeakHours")
    for result in cursor.stored_results():
        dataset = result.fetchall()
        columns = [desc[0] for desc in result.description]
        print("Columns:", columns)
        print("PeakHours Data:")
        for row in dataset:
            print(row)

    # Task 3: Implement GuestStatus stored procedure
    guest_status_query = """
    CREATE PROCEDURE GuestStatus()
    BEGIN
        SELECT 
            CONCAT(GuestFirstName, ' ', GuestLastName) AS GuestName,
            CASE 
                WHEN Role IN ('Manager', 'Assistant Manager') THEN 'Ready to pay'
                WHEN Role = 'Head Chef' THEN 'Ready to serve'
                WHEN Role = 'Assistant Chef' THEN 'Preparing Order'
                WHEN Role = 'Head Waiter' THEN 'Order served'
                ELSE 'Unknown'
            END AS OrderStatus
        FROM Bookings
        LEFT JOIN Employees ON Bookings.EmployeeID = Employees.EmployeeID;
    END;
    """
    cursor.execute("DROP PROCEDURE IF EXISTS GuestStatus;")
    cursor.execute(guest_status_query)
    print("Stored procedure GuestStatus created.")

    # Run GuestStatus procedure
    cursor.callproc("GuestStatus")
    for result in cursor.stored_results():
        dataset = result.fetchall()
        columns = [desc[0] for desc in result.description]
        print("Columns:", columns)
        print("GuestStatus Data:")
        for row in dataset:
            print(row)

except Error as e:
    print("An error occurred:", e)

finally:
    # Close cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
        print("Cursor closed.")
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection returned to the pool.")
