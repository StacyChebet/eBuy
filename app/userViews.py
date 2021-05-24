from app import app
from flask import render_template

@app.route('/userLogin')
def userLogin():
    return render_template('user/userLogin.html')

@app.route('/user/Profile')
def userProfile():
    return render_template('user/userProfile')

@app.route('/eBuy/Home')
def home():
    return render_template('user/home.html')

