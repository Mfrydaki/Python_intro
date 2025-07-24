
from mysql.connector import Error
import mysql.connector

def create_connection(host_name, user_name, user_password, db_name, port):
    conn = None

    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name, 
            port = port
        )
        print("Connection to MySQL succesful")
    except Error as e:
        print(f"Error {e} occured")
    return connection


def create_table(connection):
     create_teachers_table = """
     CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY,
        firstname VARCHAR(50),
        lastname VARCHAR(50),
        age INTEGER
    )
    """
    
     create_students_table = """
     CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        firstname VARCHAR(50),
        lastname VARCHAR(50)
    )
    """
     cursor = connection.cursor()

     try:
         cursor.execute("BEGIN")
         cursor.execute(create_students_table)
         cursor.execute(create_teachers_table)
         connection.commit()
         print(f"Tables created")
     except Error as e:
         print(f"Error {e} occured")
         connection.close()
     finally:
          cursor.close()         

def main():
    conn = create_connection('lohalhost', 'user_name', 'password', 'db_name', 'port')

    if conn:
        create_table(connection = conn)
        conn.close()
        print("MySQL connection is closed")



if __name__ == "__main__":
    main()