import DB.user_auth as auth
import DB.conn as conn

# When a script is run directly from the command line, the special variable __name__ is set to __main__.
# This is not the case when the script is imported as a module.
if __name__=="__main__":
    try:
        db=conn.connect()
        cursor = db.cursor()
        # auth.login(cursor)
        auth.register(cursor, db)
    except Exception as e:
        print(f"An error occured: {e}")

    # Closing the db connection after the login is done
    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()