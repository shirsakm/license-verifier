from flask import Flask, session, redirect, url_for
from auth import auth

app = Flask(__name__)
app.secret_key = 'secret'
app.register_blueprint(auth, url_prefix='/auth')

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f'Welcome {session["user"]}!'
    return redirect(url_for('auth.login'))


if __name__ == '__main__':  
    app.run(debug=True)