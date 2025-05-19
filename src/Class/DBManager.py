import mysql.connector
class DBManager:
    def __init__(self, host="localhost", user="root", password="", database="LinQ-SEProject"):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    def  close(self):
        self.conn.close()

    def create_user(self, username, password, firstname, lastname):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, firstname, lastname) VALUES (%s, %s, %s, %s)", (username, password, firstname, lastname))
            self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "User created successfully"
        finally:
            cursor.close()

    def create_business(self, name, owner, logo=None):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO business (name, owner, logo) VALUES (%s, %s, %s)", (name, owner, logo))
            self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "Business created successfully"
        finally:
            cursor.close()