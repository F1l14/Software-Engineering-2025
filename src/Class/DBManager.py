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

    def login(self, username, password):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def createUser(self, username, password, firstname, lastname):
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

    def createEmployee(self, username, department):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO employees (username, department) VALUES (%s, %s)", (username, department))
            self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "Employee created successfully"
        finally:
            cursor.close()


    def createBusiness(self, name, owner, logo=None):
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

    def createDepartment(self, name):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO departments (name) VALUES (%s)", (name,))
            self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "Department created successfully"
        finally:
            cursor.close()
    

    def createTeam(self, name, department, leader):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO teams (name, department, leader) VALUES (%s, %s, %s)", (name, department, leader))
            self.conn.commit()
            self.new_member(cursor.lastrowid, leader)
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "Team created successfully"
        finally:
            cursor.close()

    def newMember(self, team_id, member):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO team_members (team_id, member) VALUES (%s, %s)", (team_id, member))
            self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "Member added successfully"
        finally:
            cursor.close()

    def createTask(self, team_id, name, assigned_to):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO tasks (team_id, name, assigned_to) VALUES (%s, %s, %s)", (team_id, name, assigned_to,))
            self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "Task created successfully"
        finally:
            cursor.close()