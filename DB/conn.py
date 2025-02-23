import mysql.connector
"""
pip install mysql-connector-python

need to commit after every transaction that alters data ( not needed in SELECT queries)
"""
def connect():
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythonDB"
    )
    
    return db
