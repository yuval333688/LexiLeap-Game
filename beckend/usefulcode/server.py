from flask import Flask, jsonify, g
from flask_cors import CORS

# Assuming the functions are in these files, adjust if necessary
from getLevel import getWordsInLevel
from storage.DatabaseManager import DatabaseManager
from user_progress_service import getUserLevelsInformation

app = Flask(__name__)
CORS(app)

# --- Database Connection Handling ---

def get_db():
    """
    Opens a new database connection if one is not already open for the current request.
    The connection is stored in Flask's 'g' object, which is unique for each request.
    """
    # Check if a 'db' object is not already in the request context ('g')
    if 'db' not in g:
        # If not, create a new DatabaseManager instance and store it
        g.db = DatabaseManager()
        # Ensure the connection was successfully established
        if g.db.connection is None:
            # If the connection failed, set it to None to prevent further use
            g.db = None
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    """
    Closes the database connection at the end of the request.
    This function is automatically called by Flask.
    """
    # Pop the 'db' object from the request context, safely returning None if it's not there
    db = g.pop('db', None)

    # The __del__ method in the DatabaseManager class will be called automatically
    # when the 'db' object is garbage collected (popped from 'g'), which closes the connection.
    # No explicit close call is needed here if __del__ is implemented.
    if db is not None:
        # This print statement is for debugging to confirm the teardown is working.
        print("Database connection teardown successful.")


# --- API Routes ---

@app.route("/")
def say_hi():
    """A simple route to confirm the server is running."""
    return "Hello, World!"


@app.route("/getLevel/<int:level_num>")
def get_level_words(level_num):
    """
    An endpoint to get a list of words for a specific level.
    """
    try:
        words = getWordsInLevel(level_num)
        return jsonify(words)
    except IndexError:
        # This is appropriate if getWordsInLevel raises IndexError for an invalid level
        return jsonify({"error": "Level number out of range"}), 404
    except Exception as e:
        # General error handler
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500


@app.route("/user_progress/<int:user_id>")
def get_user_progress(user_id):
    """
    An endpoint to get all completed level information for a specific user.
    """
    # Get a database connection from the request context
    db = get_db()
    if db is None:
        # If the database connection fails, return a server error
        return jsonify({"error": "Could not connect to the database"}), 503 # Service Unavailable

    try:
        # Call the function to fetch data, passing the database manager instance
        progress_data = getUserLevelsInformation(user_id, db)
        
        if progress_data is None:
            # This could mean a database error occurred inside the function
            return jsonify({"error": "Failed to retrieve user progress"}), 500
        
        # It's good practice to return an empty list if a user simply has no progress yet
        return jsonify(progress_data)
        
    except Exception as e:
        # Catch any other unexpected errors during execution
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500


if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=5000, debug=True)