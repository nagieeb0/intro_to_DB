# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # or your MySQL server host
            user='your_username',  # replace with your MySQL username
            password='your_password'  # replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            cursor.execute("USE alx_book_store")
            
            # Create tables
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Authors (
                    author_id INT AUTO_INCREMENT PRIMARY KEY,
                    author_name VARCHAR(215) NOT NULL
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Books (
                    book_id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(130) NOT NULL,
                    author_id INT,
                    price DOUBLE,
                    publication_date DATE,
                    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Customers (
                    customer_id INT AUTO_INCREMENT PRIMARY KEY,
                    customer_name VARCHAR(215) NOT NULL,
                    email VARCHAR(215) NOT NULL,
                    address TEXT
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Orders (
                    order_id INT AUTO_INCREMENT PRIMARY KEY,
                    customer_id INT,
                    order_date DATE,
                    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
                )
            """)
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Order_Details (
                    orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
                    order_id INT,
                    book_id INT,
                    quantity DOUBLE,
                    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                    FOREIGN KEY (book_id) REFERENCES Books(book_id)
                )
            """)
            
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
