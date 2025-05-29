from flask import Flask
from flask_cors import CORS
# Use a relative import because utilities.py is in the same directory
from .utilities import getWords, getProgressData



app = Flask(__name__)
CORS(app)

# --- Database Connection Handling ---



# --- API Routes ---

@app.route("/")
def hello_world():
    """A simple route to confirm the server is running."""
    return "Hello, World!"


@app.route("/getLevel/<int:level_num>")
def get_level_words(level_num):
    return getWords(level_num)


@app.route("/user_progress/<int:user_id>")
def get_user_progress(user_id):
   return getProgressData(user_id)


if __name__ == '__main__':
   
    app.run(host='127.0.0.1', port=5000, debug=True)