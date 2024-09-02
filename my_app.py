from flask import Flask, request, session, redirect, url_for, render_template, abort
from functools import wraps

app = Flask(__name__)
app.secret_key = 'secret_key'

# Simulated user database
users = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'user': {'password': 'user123', 'role': 'user'},
    'guest': {'password': 'guest123', 'role': 'guest'}
}

blacklist = ['192.168.1.100']  # Example of an IP address being blacklisted

# Role access control decorator
def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get('role') != role:
                abort(403)  # Return 403 Forbidden
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

# IP blacklist check decorator
def ip_check(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.remote_addr in blacklist:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

# Root path route
@app.route('/')
def index():
    return 'Welcome to the home page'

# Handle favicon requests
@app.route('/favicon.ico')
def favicon():
    return '', 204

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = users.get(username)
    if user and user['password'] == password:
        session['role'] = user['role']
        return redirect(url_for('home'))
    return 'Login Failed'

# Home page route
@app.route('/home')
@ip_check
def home():
    return 'Welcome to the home page'

# Admin page route
@app.route('/admin')
@role_required('admin')
@ip_check
def admin():
    return 'Welcome to the admin page'

if __name__ == '__main__':
    app.run(debug=True)
