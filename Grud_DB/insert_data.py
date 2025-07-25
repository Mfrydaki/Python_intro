
import mysql.connector
from mysql.connector import Error  

def create_connection(host_name, user_name, user_password, db_name, port):
    """
        Create a database connection to a MySQL server.
        
        Parameters:
        host_name (str): The name of the host.
        user_name (str): The user name used to authenticate.
        user_password (str): The password used to authenticate.
        db_name (str): The name of the database.
        port (str): The port number to connect to.

        Returns:
        conn: A MySQLConnection object or None if the connection failed.
        """
    connection = None

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

def insert_teacher(connection, teacher):
    """
    Insert a teacher into the teachers table.

    Parameters:
    connection: A MySQLConnection object.
    teacher (tuple): A tuple containing the teacher's id, firstname, lastname, and age.
    """

    cursor = connection.cursor()
    
    try:
        cursor.execute( "INSERT INTO teachers (id, firstname, lastname, age) VALUES (%s, %s, %s, %s)",teacher
        )
        connection.commit()
        print("Teacher inserted successfully")
    except Error as e:
         print(f"Error: '{e}' occurred")
         connection.rollback()
    finally:
          cursor.close()

def main():
        """
        Main function to connect to the database and insert a teacher.
        """
        conn = create_connection(('lohalhost', 'user_name', 'password', 'db_name', 'port'))
        if conn:
            teacher = (2, "Bob", "M.", 55)
            insert_teacher(conn, teacher)
            conn.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
  main()