
import mysql.connector

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!@#$1234Ab"
)

cursor = conn.cursor()

# Create a database
cursor.execute("DROP DATABASE IF EXISTS demo;")

print("Database dropped successfully!")

# Close connection
cursor.close()
conn.close()