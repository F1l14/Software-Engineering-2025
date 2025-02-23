# cursor.execute("SELECT * FROM %s" % ("users"))

def login(cursor):
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    if cursor.fetchone():
        print("Login successful")
    else:
        print("Wrong cresecentials")

def register(cursor, db):
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        print("User registered successfully")
    except Exception as e:
        print(f"An error occured: {e}")