import mysql.connector

# MySQL connection settings
conn = mysql.connector.connect(
    host="localhost",
    user="rishikesh",  # Replace with your MySQL username
    password=""  # Replace with your MySQL password
)

cursor = conn.cursor()

database="mydatabase"  # Replace with your database name
table ="mytable"       # Replace with your table name 

# Create a databasse
try:
	cursor.execute(f"CREATE DATABASE {database}")
except Exception:
	pass

# Select/Use the database
cursor.execute(f"USE {database}")

# Create a table
try:
	cursor.execute(f"CREATE TABLE {table}(name varchar(50), age int(10), city varchar(50))") 
except Exception:
	pass

# Add data

add_data = (f"INSERT INTO {table}(name, age, city) VALUES(%s, %s, %s)")

cursor.execute(add_data, ("John", 30, "New York"))
cursor.execute(add_data, ("Rishi", 20, "Nashik"))

conn.commit()
print("Data added.")


# Query data
query = f"SELECT * FROM {table} WHERE name = %s"
cursor.execute(query, ("John",))
result = cursor.fetchone()
print("Data found:", result)

# Update data

update_data = (f"UPDATE {table} SET age = %s WHERE name = %s")
data_to_update = (31, "John")

cursor.execute(update_data, data_to_update)
conn.commit()
print("Data updated.")


# Display all rows in the table
cursor.execute(f"SELECT * FROM {table};")
for row in cursor.fetchall():
    print(row)

# Delete data

delete_data = (f"DELETE FROM {table} WHERE name = %s")
cursor.execute(delete_data, ("John",))
conn.commit()
print("Data deleted.")


cursor.close()
conn.close()


# Create a New USER

"""
sudo mysql -u root

mysql> USE mysql;
mysql> CREATE USER 'YOUR_SYSTEM_USER'@'localhost' IDENTIFIED BY 'YOUR_PASSWD';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'YOUR_SYSTEM_USER'@'localhost';
mysql> UPDATE user SET plugin='auth_socket' WHERE User='YOUR_SYSTEM_USER';
mysql> FLUSH PRIVILEGES;
mysql> exit;

sudo service mysql restart
"""
