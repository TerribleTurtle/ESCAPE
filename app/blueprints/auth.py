from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)


# IS MISSING LOGIC


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Add logic to authenticate user here
        flash('Login successful!', 'success')
        return redirect(url_for('splash_screen'))
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    # Add logic to log out user here
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
