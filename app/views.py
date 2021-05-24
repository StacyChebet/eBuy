from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login As')
def login():
    return render_template('auth/loginAs.html')

@app.route('/sign Up')
def signUp():
    return render_template('auth/signUp.html')

@app.route('/eBuy/about Us')
def aboutUs():
    return render_template('aboutUs.html')

@app.route('/eBuy/contact Us')
def contactUs():
    return render_template('contactUs.html')