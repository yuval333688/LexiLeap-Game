from flask import jsonify, g
from ..storage.DatabaseManager import DatabaseManager # שתי נקודות
from ..model.getLevel import getWordsInLevel         # שתי נקודות
from ..model.user_progress import getUserLevelsInformation # שתי נקודות


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






def getWords(level_num: int):
    """
    An endpoint to get a list of words for a specific level.
    """
    try:
        words = getWordsInLevel(level_num)
        return jsonify(words)
    except Exception as e:
        # General error handler
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500



def getProgressData(user_id):
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
