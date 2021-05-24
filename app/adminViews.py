from app import app
from flask import render_template

@app.route('/admin/login')
def adminLogin():
    return render_template('admin/adminLogin.html')

@app.route('/admin/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')

@app.route('/admin/profile')
def adminProfile():
    return render_template('admin/adminProfile.html')