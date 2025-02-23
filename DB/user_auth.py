# cursor.execute("SELECT * FROM %s" % ("users"))

def login(cursor):
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    if cursor.fetchone():
        print("Login successful")
    else:
        print("Wrong cresecentials")