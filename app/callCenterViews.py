from app import app
from flask import render_template

@app.route('/callCenterStaff/login')
def callCenterStaffLogin():
    return render_template('callCenter/callCenterStaffLogin.html')