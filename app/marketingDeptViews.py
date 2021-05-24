from app import app
from flask import render_template

@app.route('/marketingDepartment/login')
def marketingStaffLogin():
    return render_template('marketingDepartment/marketingDeptLogin.html')