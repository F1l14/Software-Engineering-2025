import DB.user_auth as auth
import DB.conn as conn
from auth_window import auth_window
from PyQt5.QtWidgets import QApplication

current_user = None
# When a script is run directly from the command line, the special variable __name__ is set to __main__.
# This is not the case when the script is imported as a module.
if __name__=="__main__":
    try:
        db=conn.connect()
        cursor = db.cursor()
        #current_user=auth.login(cursor, db)
        #auth.register(cursor, db)

        # print(current_user)
        
        app = QApplication([])
        window = auth_window(cursor, db)
        window.show()
        app.exec_()

    
    except Exception as e:
        print(f"An error occured: {e}")

    # Closing the db connection after the login is done
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()