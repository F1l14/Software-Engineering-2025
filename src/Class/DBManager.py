import mysql.connector
import json


class DBManager:
    def __init__(self, host="localhost", user="root", password="", database="LinQ-SEProject"):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            use_pure=True
        )
        
    def classifyUser(self, username):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT 'employee' AS role FROM employees WHERE username = %s
                UNION
                SELECT 'manager' AS role FROM managers WHERE username = %s
                UNION
                SELECT 'admin' AS role FROM business WHERE owner = %s
            """, (username, username, username))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()


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

    def createUser(self, username, password, firstname, lastname, role=None, department=None):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, firstname, lastname) VALUES (%s, %s, %s, %s)", (username, password, firstname, lastname))
            self.conn.commit()

            if role == "employee":
                cursor.execute("INSERT INTO employees (username, department) VALUES (%s, %s)", (username, department))
                self.conn.commit()
            elif role == "manager":
                cursor.execute("INSERT INTO managers (username, department) VALUES (%s, %s)", (username, department))
                self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "OK"
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
            return "OK"
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

    def createDepartment(self, name):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO departments (name) VALUES (%s)", (name,))
            self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "OK"
        finally:
            cursor.close()


    """def createTeam(self, name, department, leader):
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
            cursor.close()"""

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

    def queryDepartments(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT name FROM departments")
        
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return "ERROR"
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
            return "OK"
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
            return "OK"
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
            return "OK"
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

    def queryMyProjects(self, username):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT projects.*
                FROM projects
                LEFT JOIN project_departments ON projects.id = project_departments.project_id
                LEFT JOIN departments ON departments.name = project_departments.department_name
                LEFT JOIN managers ON departments.name = managers.department
                WHERE managers.username = %s
            """, (username,))
            
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()  

    def queryProjectTeams(self, project_data, manager):
        project_id = project_data['id']
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT DISTINCT teams.*
                FROM teams
                LEFT JOIN project_departments 
                ON TRIM(LOWER(teams.department)) = TRIM(LOWER(project_departments.department_name))
                WHERE project_departments.project_id = %s
                OR TRIM(LOWER(teams.department)) = (
                    SELECT TRIM(LOWER(department))
                    FROM managers
                    WHERE username = %s
                );
            """, (project_id, manager))
            
            result = cursor.fetchall()
            print("Teams found:", result)
            return result
        except mysql.connector.Error as err:
            print("Error:", err)
            return []
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

    def queryAvailableEmployees(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT e.username
                FROM employees e
                WHERE e.username NOT IN (
                    SELECT member FROM team_members
                )
                AND e.username NOT IN (
                    SELECT username FROM managers
                )
            """)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
 

    def createProject(self, selected_names, projectDetails):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO projects (name, description, deadline, value) VALUES (%s, %s, %s, %s)",
                (projectDetails[0], projectDetails[1], projectDetails[2], projectDetails[3])
            )
            project_id = cursor.lastrowid  

            for dept_name in selected_names:
                cursor.execute(
                    "INSERT INTO project_departments (project_id, department_name) VALUES (%s, %s)",
                    (project_id, dept_name)
                )

            self.conn.commit()
        except mysql.connector.Error as err:
            self.conn.rollback()  
            return f"Error: {err}"
        else:
            return "Project created and departments assigned successfully"
        finally:
            cursor.close()

    def createTeam(self, selected_members, selected_leader, name, username):
        cursor = self.conn.cursor()
        try:
      
            cursor.execute("SELECT department FROM managers WHERE username = %s", (username,))
            result = cursor.fetchone()
            if not result:
                return "Manager not found."
            department = result[0]

            cursor.execute(
                "INSERT INTO teams (name, department, leader) VALUES (%s, %s, %s)",
                (name, department, selected_leader)
            )

            team_id = cursor.lastrowid

            for member in selected_members:
                cursor.execute(
                    "INSERT INTO team_members (team_id, member) VALUES (%s, %s)",
                    (team_id, member)
                )

            self.conn.commit()
        except mysql.connector.Error as err:
            self.conn.rollback()
            return f"Error: {err}"
        else:
            return "Team created successfully"
        finally:
            cursor.close()


    def updateProject(self, updated_data):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "UPDATE projects SET name = %s, description = %s, deadline = %s, value = %s WHERE id = %s",
                (
                    updated_data["name"],
                    updated_data["description"],
                    updated_data["deadline"],
                    updated_data["value"],
                    updated_data["id"]
                )
            )

            self.conn.commit()
        except mysql.connector.Error as err:
            self.conn.rollback()
            return f"Error: {err}"
        else:
            return "Project updated successfully"
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
    ####       
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



    #-----------------Use case 4-----------------------
    def queryMessages(self, username):
        cursor = self.conn.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT id, name, user_1, user_2
                FROM messages_history
                WHERE user_1 = %s OR user_2 = %s
                ORDER BY id DESC
            """, (username, username))
            return cursor.fetchall()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    # Use Case 7:
    def queryEmployeeSalaries(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT username, salary FROM employees")
            result = cursor.fetchall()
            return result

        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()


    #Αναζήτηση receiver για δημιουργία συνομιλίας
    def queryReceiver(self, searchText):
        cursor = self.conn.cursor(dictionary=True)  #για να επιστρέψει λεξικό
        try:
            search_pattern = f"%{searchText}%"
            query = """
                SELECT username, firstname, lastname 
                FROM users 
                WHERE username LIKE %s OR firstname LIKE %s OR lastname LIKE %s
            """
            cursor.execute(query, (search_pattern, search_pattern, search_pattern))
            results = cursor.fetchall()
            return results  # Επιστρέφει λίστα από λεξικά
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def checkBonusState(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT state FROM bonus_state")
            result = cursor.fetchone()  # Use fetchone instead of fetchall
            return result[0] if result else None

        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()


    #Απόκτηση chat ID
    def get_chat_id(self, user1, user2):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT id FROM messages_history
                WHERE (user_1 = %s AND user_2 = %s) OR (user_1 = %s AND user_2 = %s)
            """, (user1, user2, user2, user1))
            result = cursor.fetchone()
            return result[0] if result else None
        finally:
            cursor.close()

    #Δημιουργία Νέας Συνομιλίας
    def create_chat(self, name, user1, user2):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO messages_history (name, user_1, user_2, history)
                VALUES (%s, %s, %s, '[]')
            """, (name, user1, user2))
            self.conn.commit()
            return cursor.lastrowid
        finally:
            cursor.close()

    #Ιστορικό Συνομιλίας
    def get_chat_history(self, chat_id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT history FROM messages_history WHERE id = %s", (chat_id,))
            result = cursor.fetchone()
            if result:
                return json.loads(result[0])
            return []
        finally:
            cursor.close()

    #Εισαγωγή νέου μηνύματος
    def insert_message(self, chat_id, message_obj):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT history FROM messages_history WHERE id = %s", (chat_id,))
            result = cursor.fetchone()
            if not result:
                return
            history = json.loads(result[0])
            history.append(message_obj)
            cursor.execute("UPDATE messages_history SET history = %s WHERE id = %s", (json.dumps(history), chat_id))
            self.conn.commit()
        finally:
            cursor.close()

    #Απόκτηση χρήστη
    def get_user_by_username(self, username):
        cursor = self.conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            return cursor.fetchone()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()


    #USE CASE 5:
    def saveEvaluationForm(self, type, start_date, end_date):
            cursor = self.conn.cursor()

            try:
                cursor.execute("INSERT INTO evaluation_forms (type, start_date, end_date) VALUES (%s, %s, %s)", (type, start_date, end_date))
                self.conn.commit()
            except mysql.connector.Error as err:
                return f"Error: {err}"
            else:
                eval_id = cursor.lastrowid
                return "Evaluation saved successfully", eval_id
            finally:
                cursor.close()

    def saveQuestion(self, eval_id, question_text, answers):
            cursor = self.conn.cursor()

            try:
                cursor.execute("INSERT INTO evaluation_questions (eval_id, question_text, answers) VALUES (%s, %s, %s)", (eval_id, question_text, ','.join(answers)))
                self.conn.commit()
            except mysql.connector.Error as err:
                return f"Error: {err}"
            else:
                return "Question saved successfully"
            finally:
                cursor.close()
    
    def queryAllManagers(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT username FROM users INNER JOIN managers ON users.username = managers.username")
            result = cursor.fetchall()
            return [row[0] for row in result]
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()



    
    # Use Case 6:
    def queryTeams(self, username):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT 
                    t.id AS team_id, 
                    t.name AS team_name 
                FROM teams t
                INNER JOIN team_members tm ON t.id = tm.team_id
                WHERE tm.member = %s
            """, (username,))
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def queryEvaluationForm(self, type):
        cursor = self.conn.cursor()
        try:
                cursor.execute("""
                    SELECT 
                        f.eval_id AS form_id,
                        q.question_id AS question_id,
                        q.question_text,
                        q.answers
                    FROM evaluation_forms f
                    JOIN evaluation_questions q ON f.eval_id = q.eval_id
                    WHERE f.type = %s
                    AND f.eval_id = (
                        SELECT MAX(eval_id)
                        FROM evaluation_forms
                        WHERE type = %s
                    )
                """, (type,type))
                return cursor.fetchall()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def saveEvaluationAnswer(self, eval_id, username, eval_for, question_id, answer):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO evaluation_answers (eval_id, username, eval_for, question_id, answers) VALUES (%s, %s, %s, %s, %s)", (eval_id, username, eval_for, question_id, answer))
            self.conn.commit()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        else:
            return "Answer saved successfully"
        finally:
            cursor.close()
            
    def queryManagerEmployees(self, manager_username):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT e.username, u.firstname, u.lastname
                FROM employees e
                INNER JOIN users u ON e.username = u.username
                INNER JOIN managers m ON e.department = m.department
                WHERE m.username = %s
            """, (manager_username,))
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def queryManager(self, username):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT m.username FROM managers m INNER JOIN employees e ON m.department = e.department WHERE e.username = %s", (username,))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def getEvaluationEndDate(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT end_date FROM evaluation_forms ORDER BY eval_id DESC LIMIT 1")
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def isEvaluationActive(self, user_type):
        cursor = self.conn.cursor()
        try:
            eval_type = 'eval_for_employees' if user_type == 'manager' else 'eval_for_managers'

            cursor.execute("""
                SELECT COUNT(*) FROM evaluation_forms 
                WHERE type = %s AND NOW() BETWEEN start_date AND end_date
            """, (eval_type,))
            result = cursor.fetchone()
            if result[0] > 0:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            

    def employeeHasAnswered(self, username):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM evaluation_answers WHERE username = %s", (username,))
            result = cursor.fetchone()
            return result[0] > 0
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
    #END OF USE CASE 5
    
    # Use Case 6:
    def queryTeams(self, username):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT 
                    t.id AS team_id, 
                    t.name AS team_name 
                FROM teams t
                INNER JOIN team_members tm ON t.id = tm.team_id
                WHERE tm.member = %s
            """, (username,))
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()



    def createBonusDetails(self, badget_numbers, perc1, perc2):
        cursor = self.conn.cursor(dictionary=True)
        try:
            for i in range(len(badget_numbers)):
                cursor.execute(
                    "INSERT INTO bonus_setup (category_value, manager_bonus_percentage, employee_bonus_percentage) VALUES (%s, %s, %s)",
                    (badget_numbers[i], perc1[i], perc2[i])
                )

            cursor.execute("UPDATE bonus_state SET state = 'active'")

            self.conn.commit()
        except mysql.connector.Error as err:
            self.conn.rollback()
            return f"Error: {err}"
        else:
            return "Bonus setup saved and activated successfully"
        finally:
            cursor.close()

    def queryBonusBoardDetails(self):
        cursor = self.conn.cursor(dictionary=True)
        try:
            # 1. Load bonus setup (ordered by threshold)
            cursor.execute("SELECT category_value, manager_bonus_percentage, employee_bonus_percentage FROM bonus_setup ORDER BY category_value ASC")
            bonus_setup = cursor.fetchall()

            # 2. Get project value for each department
            cursor.execute("SELECT pd.department_name, SUM(p.value) AS total_value FROM project_departments pd JOIN projects p ON pd.project_id = p.id GROUP BY pd.department_name")
            dept_project_values = {row["department_name"]: row["total_value"] for row in cursor.fetchall()}

            # 3. Load employees
            cursor.execute("SELECT username, department, salary FROM employees")
            employees = cursor.fetchall()

            # 4. Load managers
            cursor.execute("SELECT username FROM managers")
            manager_usernames = {row["username"] for row in cursor.fetchall()}

            bonus_board_results = []

            # 5. Calculate bonuses
            for emp in employees:
                username = emp["username"]
                department = emp["department"]
                salary = emp["salary"]
                role = "manager" if username in manager_usernames else "employee"
                project_value = dept_project_values.get(department, 0)

                # Determine bonus percentage from bonus_setup
                bonus_percentage = 0.0
                for setup in bonus_setup:
                    if project_value < setup["category_value"]:
                        bonus_percentage = setup["manager_bonus_percentage"] if role == "manager" else setup["employee_bonus_percentage"]
                        break
                else:
                    # Use last row if value exceeds all thresholds
                    last = bonus_setup[-1]
                    bonus_percentage = last["manager_bonus_percentage"] if role == "manager" else last["employee_bonus_percentage"]

                bonus_amount = round(salary * (bonus_percentage / 100.0), 2)

                bonus_board_results.append({
                    "username": username,
                    "role": role,
                    "salary": salary,
                    "bonus": bonus_amount
                })

            return (bonus_board_results, bonus_setup)

        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def updateSalariesList(self, updated_data):
        try:
            cursor = self.conn.cursor()

            update_query = "UPDATE employees SET salary = %s WHERE username = %s"

            # Convert to (salary, username) tuples for query execution
            update_values = [(salary, username) for username, salary in updated_data]

            cursor.executemany(update_query, update_values)
            self.conn.commit()

            print(f"{cursor.rowcount} salaries updated successfully.")
            return "Salaries updated successfully."

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return f"Database error: {err}"

        finally:
            cursor.close()
            
    def queryTasksOfTeam(self, team_id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT 
                    t.id AS task_id, 
                    t.task_name, 
                    t.assigned_to, 
                    t.state 
                FROM tasks t
                WHERE t.team_id = %s
            """, (team_id,))
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def queryEvents(self, team_space_id):
        pass

    def queryNoticeboard(self, team_space_id):
        pass



    #-----------------Use case 10-----------------------
    def queryAvailableNotices(self):
        cursor = self.conn.cursor(dictionary=True)
        try:
            cursor.execute("""
               SELECT id, title, type, created
                FROM notices
                ORDER BY id DESC
            """)
            return cursor.fetchall()
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    #USE CASE 9
    def queryUserLeaveRequests(self, username):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT leave_request_id, start_date, end_date, state
                FROM employee_leave_request 
                WHERE user = %s
            """, (username,))
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()



    def loadNotice(self):
        cursor = self.conn.cursor(dictionary=True)
        try:
            cursor.execute(""" 
                SELECT title, type, created, body 
                FROM notices 
                WHERE id = %s
            """,  (self.notice_id,))
            notice = cursor.fetchone()
            if notice:
                if self.titleLabel:
                    self.titleLabel.setText(notice.get("title", ""))
                if self.typeLabel:
                    self.typeLabel.setText(notice.get("type", ""))
                if self.createdLabel:
                    created = notice.get("created")
                    if created and hasattr(created, "strftime"):
                        self.createdLabel.setText(created.strftime("%Y-%m-%d %H:%M"))
                    else:
                        self.createdLabel.setText(str(created) if created else "")
                if self.bodyLabel:
                    self.bodyLabel.setText(notice.get("body", ""))
        finally:
            cursor.close()

    def insertNotice(self, notice_type, title, body):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO notices (type, title, body)
                VALUES (%s, %s, %s)
            """, (notice_type, title, body))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()
            
    def insertLeaveRequest(self, user, start_date, end_date, reason):
        cursor = self.conn.cursor()
        try:
            cursor.execute("INSERT INTO employee_leave_request (user, start_date, end_date, reason,state) VALUES (%s, %s, %s, %s,%s)", (user, start_date, end_date, reason,"Pending"))
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
    
    def checkLeaveCapability(self, user):
        cursor = self.conn.cursor()
        try:
            cursor.execute("SELECT COUNT(*) FROM employee_leave_request WHERE user = %s AND state = 'Pending'", (user,))
            result = cursor.fetchone()
            return result[0] == 0
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
    
    def queryDepartmentLeaveRequests(self, manager_username):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT elr.leave_request_id, elr.user, elr.start_date, elr.end_date, elr.reason
                FROM employee_leave_request elr
                INNER JOIN employees e ON elr.user = e.username
                INNER JOIN managers m ON e.department = m.department
                WHERE m.username = %s AND elr.state = 'Pending'
            """, (manager_username,))
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
    
    def queryDepartmentLeaves(self, manager_username):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT user, start_date, end_date
                FROM employee_leave
                INNER JOIN employees e ON employee_leave.user = e.username
                INNER JOIN managers m ON e.department = m.department
                WHERE m.username = %s
            """, (manager_username,))
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def queryLeaveRequestById(self, request_id):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT user, start_date, end_date, reason
                FROM employee_leave_request 
                WHERE leave_request_id = %s
            """, (request_id,))
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
    
    def checkSameDateRequests(self, employee, start_date, end_date):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                SELECT user, start_date, end_date
                FROM employee_leave_request 
                WHERE user != %s AND state = 'Accepted' AND (
                    (start_date <= %s AND end_date >= %s) OR
                    (start_date <= %s AND end_date >= %s) OR
                    (start_date >= %s AND end_date <= %s)
                )
            """, (employee, start_date, start_date, end_date, end_date, start_date, end_date))
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def saveRequest(self, employee, start_date, end_date):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                UPDATE employee_leave_request
                SET state = 'Accepted'
                WHERE user = %s AND start_date = %s AND end_date = %s
            """, (employee, start_date, end_date))
            cursor.execute("""
                INSERT INTO employee_leave (user, start_date, end_date)
                VALUES (%s, %s, %s)
            """, (employee, start_date, end_date))
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()

    def saveDeclinedRequest(self, employee, start_date, end_date, decline_reason):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                UPDATE employee_leave_request
                SET state = 'Declined', reason = %s
                WHERE user = %s AND start_date = %s AND end_date = %s
            """, (decline_reason, employee, start_date, end_date))
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
    #END OF USE CASE 9

    def queryUserType(self, username):
        cursor = self.conn.cursor()
        try:

            if username == "admin":
                return "admin"


            cursor.execute("SELECT 1 FROM managers WHERE username = %s", (username,))
            is_manager = cursor.fetchone() is not None

            if is_manager:
                return "manager"


            cursor.execute("SELECT 1 FROM employees WHERE username = %s", (username,))
            is_employee = cursor.fetchone() is not None

            if is_employee:
                return "employee"

            return "unknown"

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            cursor.close()   

