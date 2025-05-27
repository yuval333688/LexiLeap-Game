import psycopg2
import configparser

class DatabaseManager:
    
    
    def __init__(self, config_file='databaseConnect.txt'):
        """
        Constructor for the DatabaseManager class.
        Initializes the database connection.
        """
        self.connection = self.connect_to_database(config_file)

    def get_db_params_from_file(self, filename):
        """
        Reads database connection parameters from a file.
        The file should be in a key=value format.
        """
        params = {}
        try:
            with open(filename, 'r') as f:
                for line in f:
                    # Ignore comments and empty lines
                    if line.strip() and not line.strip().startswith('#'):
                        key, value = line.strip().split('=', 1)
                        params[key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"Error: Configuration file '{filename}' not found.")
            return None
        except ValueError:
            print(f"Error: Invalid format in configuration file '{filename}'. Expected 'key=value'.")
            return None

        return params

    def connect_to_database(self, filename="config.txt"):
        """
        Establishes a connection to the PostgreSQL database
        using parameters from a configuration file.
        """
        db_params = self.get_db_params_from_file(filename)
        if db_params is None:
            return None
            
        try:
            # Establish a connection to the database
            conn = psycopg2.connect(**db_params)
            return conn
        except psycopg2.OperationalError as e:
            print(f"Could not connect to the database: {e}")
            return None

    # --- פונקציות חדשות ---

    def fetch_all_rows(self, query, params=None):
        """
        Executes a SELECT query and fetches all resulting rows.
        :param query: The SELECT SQL query to execute.
        :param params: (Optional) A tuple or dictionary of parameters to pass to the query.
        :return: A list of tuples representing the rows, or None if an error occurs.
        """
        if not self.connection:
            print("No database connection.")
            return None
        
        # Create a new cursor
        cursor = self.connection.cursor()
        try:
            # Execute the query
            cursor.execute(query, params)
            # Fetch all the results
            rows = cursor.fetchall()
            return rows
        except (psycopg2.Error, psycopg2.Warning) as e:
            print(f"Error executing SELECT query: {e}")
            return None
        finally:
            # Always close the cursor
            cursor.close()

    def execute_and_commit(self, query, params=None):
        """
        Executes a data modification query (INSERT, UPDATE, DELETE, CREATE) and commits the changes.
        :param query: The SQL query to execute.
        :param params: (Optional) A tuple or dictionary of parameters to pass to the query.
        :return: True if the command executed successfully, False otherwise.
        """
        if not self.connection:
            print("No database connection.")
            return False

        # Create a new cursor
        cursor = self.connection.cursor()
        try:
            # Execute the query
            cursor.execute(query, params)
            # Commit the changes to the database
            self.connection.commit()
            return True
        except (psycopg2.Error, psycopg2.Warning) as e:
            print(f"Error executing command: {e}")
            # Rollback the transaction in case of an error
            self.connection.rollback()
            return False
        finally:
            # Always close the cursor
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