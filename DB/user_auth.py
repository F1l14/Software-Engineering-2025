from os import urandom


def login(cursor, db):
    username = input("Enter username: ")
    password = input("Enter password: ")
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    if cursor.fetchone():
        token =  generate_token()
        cursor.execute("DELETE FROM user_tokens WHERE username = %s", (username,))
        db.commit()
        cursor.execute("INSERT INTO user_tokens (username, token) VALUES (%s, %s)", (username, token))
        db.commit()
        
        print("Login successful")
        # return a dictionary with username and token
        return {username:username, token:token}
    else:
        print("Wrong cresecentials")
        return None

def register(cursor, db):
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()
        print("User registered successfully")
    except Exception as e:
        print(f"An error occured: {e}")

def generate_token():
    return urandom(8).hex()