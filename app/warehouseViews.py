from app import app
from flask import render_template

@app.route('/warehouseStaff/login')
def warehouseStaffLogin():
    return render_template('warehouse/warehouseStaffLogin.html')