import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server without username and password
        connection = mysql.connector.connect(
            host='localhost'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

            # Switch to the newly created database
            cursor.execute("USE alx_book_store")

            # Read and execute the SQL file
            with open("alx_book_store.sql", "r") as sql_file:
                sql_commands = sql_file.read().split(';')  # Split commands by semicolon
                for command in sql_commands:
                    if command.strip():  # Skip empty commands
                        cursor.execute(command)

            print("Tables and schema created successfully from 'alx_book_store.sql'!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()