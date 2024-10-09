from flask import Blueprint, render_template, redirect, url_for, request, session, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Replace this with your actual user verification logic
        if username == 'admin' and password == 'password':
            session['user'] = username
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('auth/login.html')
