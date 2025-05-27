# LexiLeap-Game

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

LexiLeap is an interactive web game designed to help children and adults with dyslexia improve their writing and typing skills. The game uses a structured, level-based progression system to provide engaging exercises while tracking user performance and improvement over time via a PostgreSQL database.

## Features

-   **Interactive Level System:** Users progress through a series of numbered levels, with each level containing a unique set of words.
-   **User Progress Tracking:** The system saves each user's score for every completed level in a persistent database.
-   **Dynamic UI:** The level selection screen visually displays the status of each level (e.g., locked, open, completed) based on the user's progress.
-   **Performance Scoring:** Each level attempt is scored on a scale of 0-1000, with a score of 600 required to pass and unlock the next level.
-   **RESTful API:** A Flask-based backend serves level data and user progress information to the frontend.

## Tech Stack

-   **Backend:**
    -   **Language:** Python
    -   **Framework:** Flask
    -   **Database:** PostgreSQL
    -   **Database Driver:** Psycopg2
-   **Frontend:**
    -   HTML5, CSS3, Vanilla JavaScript

## Getting Started

Follow these instructions to get a local copy of the project up and running for development and testing purposes.

### Prerequisites

-   Python 3.x
-   PostgreSQL server installed and running
-   Git

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/LexiLeap-Game.git](https://github.com/your-username/LexiLeap-Game.git)
    cd LexiLeap-Game
    ```

2.  **Backend Setup:**
    a. It is highly recommended to create and activate a Python virtual environment in the project's root directory.
    ```sh
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
    b. Install the required Python packages:
    ```sh
    pip install Flask flask-cors psycopg2-binary
    ```
    c. **Configure the database connection:** The `DatabaseManager.py` script expects a configuration file named `databaseConnect.txt` by default. Create this file in the backend directory and add your credentials.
    ```
    dbname=new_database
    user=postgres
    password=your_postgres_password
    host=localhost
    port=5432
    ```
    d. **Initialize the Database:** Set up the database schema and seed it with initial data by running the provided SQL scripts (`01_schema.sql` and `02_seed.sql`) against your PostgreSQL instance. This will create the necessary tables and a test user.

    e. **Lesson Files:** Ensure the lesson text files (e.g., `lesson0.txt`, `lesson1.txt`) are located in the `rec/lessons/` directory, as the `getLevel.py` script expects them there. You can use the `lessensInit.py` utility script to generate these files from a master word list if needed.

    f. **Run the Flask server:**
    ```sh
    python server.py
    ```
    The server will start on `http://127.0.0.1:5000`.

3.  **Frontend Setup:**
    -   No special setup is required. Open the `index.html` file in your web browser. It will automatically redirect to the level selection screen.
    -   **Important:** Ensure you have corrected the `fetch` request in `typing_screen2.html` to use `http` instead of `https` to match the server.

## API Endpoints

The backend exposes the following main API endpoints:

-   `GET /getLevel/<int:level_num>`
    -   Fetches the words for a specific level from the corresponding `.txt` file.
-   `GET /user_progress/<int:user_id>`
    -   Retrieves a list of all levels completed by a specific user from the database.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.