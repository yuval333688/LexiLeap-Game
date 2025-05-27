from storage.DatabaseManager import DatabaseManager


def getUserLevelsInformation(user_id: int, databaseManager: DatabaseManager):
    """
    Retrieves all completed level information for a specific user from the database.

    Args:
        user_id (int): The unique identifier for the user.
        databaseManager (DatabaseManager): An active instance of the DatabaseManager class.

    Returns:
        list: A list of tuples, where each tuple represents a completed level 
              and contains (level_id, score, completed_at).
              Returns an empty list if the user has no completed levels, or None if an error occurs.
    """
    # SQL query to select all progress records for a given user, ordered by the level number.
    sql_query = """
        SELECT 
            level_id, 
            score, 
            completed_at 
        FROM 
            user_progress 
        WHERE 
            user_id = %s 
        ORDER BY 
            level_id ASC;
    """
    
    # Parameters to be safely injected into the query. It must be a tuple.
    params = (user_id,)
    
    # Execute the query using the database manager's fetch method
    try:
        results = databaseManager.fetch_all_rows(sql_query, params)
        return results
    except Exception as e:
        # Optional: Log the error for debugging purposes
        print(f"An error occurred while fetching user level information: {e}")
        return None