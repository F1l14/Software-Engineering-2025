import mysql.connector


"""
pip install mysql-connector-python

"""

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythonDB"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM users")

for item in cursor:
    print(item)
