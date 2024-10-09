from flask import Blueprint, redirect, render_template, session, url_for, request
from lify import add_license, delete_license, get_licenses

main = Blueprint('main', __name__)

@main.route('/dashboard')
def dashboard():
    if 'user' not in session:
        redirect(url_for('auth.login'))

    # Sample data for licenses
    licenses = get_licenses()
    return render_template('dashboard.html', licenses=licenses)


@main.route('/delete_license/<license_id>', methods=['POST'])
def delete_license_(license_id):
    delete_license(license_id)

    return redirect(url_for('main.dashboard'))

@main.route('/add_license', methods=['POST'])
def add_license_():
    license_id = request.form['licenseId']
    license_type = request.form['licenseType']
        
    add_license(license_id, license_type)

    return redirect(url_for('main.dashboard'))