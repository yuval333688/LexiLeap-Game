import psycopg2
import configparser
from flask import jsonify

class DatabaseManager:


    def __init__(self, config_file='config.txt'):
        """
        Constructor for the DatabaseManager class.
        Initializes the database connection.
        """
        try: 
            self.connection = self.connect_to_database(config_file)
            print("Connected to the database")
        except Exception as e:
            print(f"Error connecting to the database:/n/n/n/n/n/n/n/n {config_file} {e}")
            self.connection = None

    def connect_to_database(self, filename):
        """
        Establishes a connection to the PostgreSQL database
        using parameters from a configuration file.
        """
        db_params = self.get_db_params_from_file(filename)
        
        # Establish a connection to the database
        conn = psycopg2.connect(**db_params)
        return conn
       

    def get_db_params_from_file(self, filename):
        """
        Reads database connection parameters from a file.
        The file should be in a key=value format.
        """
        params = {}
        with open(filename, 'r') as f:
            for line in f:
                # Ignore comments and empty lines
                if line.strip() and not line.strip().startswith('#'):
                    key, value = line.strip().split('=', 1)
                    params[key.strip()] = value.strip()
        return params


    
   

    def fetch_all_rows(self, query, params=None):
        """
        Executes a SELECT query and fetches all resulting rows.
        :param query: The SELECT SQL query to execute.
        :param params: (Optional) A tuple or dictionary of parameters to pass to the query.
        :return: A list of tuples representing the rows, or None if an error occurs.
        """
        
        # Create a new cursor
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        cursor.close()
        print(jsonify(rows))
        return rows
    

    def execute_and_commit(self, query, params=None):
        """
        Executes a data modification query (INSERT, UPDATE, DELETE, CREATE) and commits the changes.
        :param query: The SQL query to execute.
        :param params: (Optional) A tuple or dictionary of parameters to pass to the query.
        :return: True if the command executed successfully, False otherwise.
        """
        if not self.connection:
            raise Exception("Database connection is not established.")

        # Create a new cursor
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
        except:
            raise Exception("Error executing command: {e}")
        finally:
            cursor.close()
       

    def __del__(self):
        """
        Destructor for the DatabaseManager class.
        This method is called when the object is about to be destroyed.
        It ensures the database connection is properly closed.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")