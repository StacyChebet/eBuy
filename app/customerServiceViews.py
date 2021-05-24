from app import app
from flask import render_template

@app.route('/customerServiceStaff/login')
def customerServiceStaffLogin():
    return render_template('customerService/customerServiceStaffLogin.html')