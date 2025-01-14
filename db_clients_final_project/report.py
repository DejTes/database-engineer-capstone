from mysql.connector import pooling, Error
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database configurations
dbconfig = {
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
}

# Task 1: Create a connection pool
try:
    pool_b = pooling.MySQLConnectionPool(pool_name="pool_b", pool_size=5, **dbconfig)
    print("Connection pool created successfully.")
except Error as e:
    print("Error while creating connection pool:", e)

# Task 2: Insert guest booking data
def insert_guest_bookings():
    try:
        # Obtain connections from the pool
        conn1 = pool_b.get_connection()
        conn2 = pool_b.get_connection()
        
        # Insert data for Guest 1 and Guest 2
        cursor1 = conn1.cursor()
        cursor2 = conn2.cursor()

        query = "INSERT INTO Bookings (TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID) VALUES (%s, %s, %s, %s, %s)"
        guest1 = (8, "Anees", "Java", "18:00", 6)
        guest2 = (5, "Bald", "Vin", "19:00", 6)
        cursor1.execute(query, guest1)
        cursor2.execute(query, guest2)

        conn1.commit()
        conn2.commit()

        print("Guest 1 and Guest 2 bookings added.")

        # Insert data for Guest 3
        try:
            conn3 = pool_b.get_connection()
            cursor3 = conn3.cursor()
            guest3 = (12, "Jay", "Kon", "19:30", 6)
            cursor3.execute(query, guest3)
            conn3.commit()
            print("Guest 3 booking added.")
        except Error as e:
            print("Error while adding Guest 3 booking:", e)
        finally:
            if 'cursor3' in locals():
                cursor3.close()
            if 'conn3' in locals() and conn3.is_connected():
                conn3.close()

    except Error as e:
        print("Error while inserting bookings:", e)
    finally:
        # Close connections
        if 'cursor1' in locals():
            cursor1.close()
        if 'cursor2' in locals():
            cursor2.close()
        if 'conn1' in locals() and conn1.is_connected():
            conn1.close()
        if 'conn2' in locals() and conn2.is_connected():
            conn2.close()

insert_guest_bookings()

# Task 3: Create a report
def create_report():
    try:
        connection = pool_b.get_connection()
        cursor = connection.cursor(buffered=True)

        # Query 1: Manager's name and EmployeeID
        query1 = """
        SELECT CONCAT(Name, ' (', Role, ')') AS ManagerName, EmployeeID 
        FROM Employees 
        WHERE Role = 'Manager';
        """ 
        cursor.execute(query1)
        manager = cursor.fetchone()

        # Query 2: Employee with the highest salary
        query2 = """
        SELECT Name AS EmployeeName, Role 
        FROM Employees 
        ORDER BY CAST(Annual_Salary AS UNSIGNED) DESC 
        LIMIT 1;
        """
        cursor.execute(query2)
        highest_paid_employee = cursor.fetchone()

        # Query 3: Guests booked between 18:00 and 20:00
        query3 = """
        SELECT COUNT(*) AS GuestCount 
        FROM Bookings 
        WHERE BookingSlot BETWEEN '18:00' AND '20:00';
        """
        cursor.execute(query3)
        guest_count = cursor.fetchone()

        # Query 4: Guests waiting to be seated
        query4 = """
        SELECT CONCAT(GuestFirstName, ' ', GuestLastName) AS GuestName, BookingID 
        FROM Bookings 
        ORDER BY BookingSlot ASC;
        """
        cursor.execute(query4)
        waiting_guests = cursor.fetchall()

        # Print the results
        print("Manager:", manager)
        print("Highest Paid Employee:", highest_paid_employee)
        print("Guests Booked Between 18:00 and 20:00:", guest_count)
        print("Waiting Guests:")
        for guest in waiting_guests:
            print(guest)

    except Error as e:
        print("Error while creating report:", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

create_report()

# Task 4: Create BasicSalesReport stored procedure
def create_basic_sales_report():
    try:
        connection = pool_b.get_connection()
        cursor = connection.cursor()

        # Create stored procedure
        procedure = """
        DROP PROCEDURE IF EXISTS BasicSalesReport;
        CREATE PROCEDURE BasicSalesReport()
        BEGIN
            SELECT 
                SUM(BillAmount) AS TotalSales,
                AVG(BillAmount) AS AverageSale,
                MIN(BillAmount) AS MinimumBill,
                MAX(BillAmount) AS MaximumBill
            FROM Orders;
        END;
        """
        cursor.execute(procedure)
        print("BasicSalesReport stored procedure created.")

    except Error as e:
        print("Error while creating stored procedure:", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

create_basic_sales_report()

# Task 5: Display next three upcoming bookings
def display_next_bookings():
    try:
        connection = pool_b.get_connection()
        cursor = connection.cursor(buffered=True)

        query = """
        SELECT BookingSlot, 
            CONCAT(GuestFirstName, ' ', GuestLastName) AS GuestName, 
            CONCAT(Employees.Name, ' [', Employees.Role, ']') AS AssignedTo
        FROM Bookings
        JOIN Employees ON Bookings.EmployeeID = Employees.EmployeeID
        ORDER BY BookingSlot ASC
        LIMIT 3;
        """
        cursor.execute(query)
        bookings = cursor.fetchall()

        # Print the results
        for booking in bookings:
            print(f"[BookingSlot] {booking[0]} | [Guest_name] {booking[1]} | [Assigned to: {booking[2]}]")

    except Error as e:
        print("Error while displaying next bookings:", e)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

display_next_bookings()
