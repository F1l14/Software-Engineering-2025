import mysql.connector
class DBManager:
    def __init__(self, host="localhost", user="root", password="", database="LinQ-SEProject"):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            use_pure=True
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

    def queryTeamMembers(self, team_id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT member FROM team_members WHERE team_id = %s", (team_id,))
            result = cursor.fetchall()
            return [row[0] for row in result]
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def queryProjects(self, leader):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT t1.name as project_name, t1.id as project_id, t2.name as team_name, t2.id as team_id, t3.member FROM projects t1 JOIN teams t2 ON t1.team_id = t2.id JOIN team_members t3 ON t2.id = t3.team_id WHERE t2.leader = %s", (leader,))
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def queryTasks(self, employee, option, state="pending"):
        cursor = self.conn.cursor(dictionary=True)
        try:
            if option == "all":
                cursor.execute("SELECT t2.name, t1.id, t1.task_name  FROM tasks t1 INNER JOIN projects t2 ON t1.project = t2.id WHERE t1.assigned_to = %s AND t1.state = %s", (employee, state))
            else:
                cursor.execute("SELECT t1.id AS task_id, t1.task_name, t1.team_id AS team_id FROM tasks t1 INNER JOIN projects t2 ON t1.project = t2.id INNER JOIN teams t3 ON t2.team_id = t3.id WHERE t1.assigned_to IS NULL AND t3.leader=%s", (employee,))
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def createTask(self, team_id, project_id, task_name, assigned_to):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO tasks (team_id, project, task_name, assigned_to) VALUES (%s, %s, %s, %s)", (team_id, project_id, task_name, assigned_to,))
            self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "Task created successfully"
        finally:
            cursor.close()

    
    def assignTask(self, task_id, assigned_to):
        cursor = self.conn.cursor()
        try:
            cursor.execute("UPDATE tasks SET assigned_to = %s WHERE id = %s", (assigned_to, task_id))
            self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "Task assigned successfully"
        finally:
            cursor.close()

    def completeTask(self, task_id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("UPDATE tasks SET state = 'completed' WHERE id = %s", (task_id,))
            self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "Task completed successfully"
        finally:
            cursor.close()

    def createNotification(self, user, type, body):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO notifications (user, type, body) VALUES (%s, %s, %s)", (user, type, body))
            self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "Notification created successfully"
        finally:
            cursor.close()
            
    #Use Case 2:
    def queryAllProjects(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * FROM projects")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()  
            
    def queryAllDepartments(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT * FROM departments")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close() 

    # Use Case 3:
    def queryBusinessData(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT 
                    DATE_FORMAT(completed_at, '%Y-%m') AS month, 
                    COUNT(*) AS completed_projects 
                FROM projects 
                WHERE status = 'completed'
                GROUP BY month
                ORDER BY month
            """)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            
    def queryAllEmployees(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                            SELECT 
                                users.username, users.firstname, users.lastname, employees.department
                            FROM users 
                            INNER JOIN employees ON users.username = employees.username
                           """)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()          
            
    def queryEmployeeProgress(self, username):
        cursor = self.conn.cursor()
        try:
            # Query project progress
            cursor.execute("""
                SELECT 
                    p.status,
                    COUNT(*) AS project_count
                FROM team_members tm
                INNER JOIN projects p ON tm.team_id = p.team_id
                WHERE tm.member = %s
                GROUP BY p.status
            """, (username,))
            columns = [col[0] for col in cursor.description]
            project_progress = [dict(zip(columns, row)) for row in cursor.fetchall()]

            # Query task progress
            cursor.execute("""
                SELECT 
                    t.state,
                    COUNT(*) AS task_count
                FROM tasks t
                WHERE t.assigned_to = %s
                GROUP BY t.state
            """, (username,))
            columns = [col[0] for col in cursor.description]
            task_progress = [dict(zip(columns, row)) for row in cursor.fetchall()]

            return {
                "projects": project_progress,
                "tasks": task_progress
            }
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
