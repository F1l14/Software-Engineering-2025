import mysql.connector


"""
pip install mysql-connector-python

need to commit after every transaction that alters data ( not needed in SELECT queries)
"""

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythonDB"
)

cursor = db.cursor()

username = input("Enter username: ")
password = input("Enter password: ")


# cursor.execute("SELECT * FROM %s" % ("users"))

cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))

# for item in cursor:
#     print(item)
if cursor.fetchone():
    print("Login successful")
else:
    print("Wrong cresecentials")