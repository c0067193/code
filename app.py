from flask import Flask, request, jsonify, make_response
import sqlite3
import re

app = Flask(__name__)



def get_db_connection():
    conn = sqlite3.connect('camera_app.db')
    conn.row_factory = sqlite3.Row
    return conn



def log_event(event_type, description):
    with open('audit.log', 'a') as f:
        f.write(f"{event_type}: {description}\n")



def is_valid_input(user_input):

    pattern = re.compile("^[a-zA-Z0-9]+$")
    return pattern.match(user_input)



@app.route('/')
def home():
    return "Welcome to the Smart Camera App!"



@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')


    if not is_valid_input(username) or not is_valid_input(password):
        log_event("InvalidInput", "Invalid characters in username or password.")
        return jsonify({"error": "Invalid input!"}), 400


    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:

        response = make_response(jsonify({"message": "Login successful!"}))
        response.set_cookie('session_id', 'secure_session_value', httponly=True, secure=True, samesite='Strict')


        log_event("LoginSuccess", f"User {username} logged in successfully.")
        return response
    else:
        log_event("LoginFailure", f"Failed login attempt for user {username}.")
        return jsonify({"error": "Invalid username or password!"}), 401


if __name__ == '__main__':
    app.run(ssl_context='adhoc')