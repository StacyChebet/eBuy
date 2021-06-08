from click import confirm
from app import app
from app import models, db
from flask import render_template, request, redirect
from flask_login import logout_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/loginAs')
def login():
    return render_template('auth/loginAs.html')

@app.route('/signUp', methods=["GET", "POST"])
def signUp():
    if request.method == "POST":
        req = request.form
        fName = req['firstName']
        lName = req['lastName']
        uName = req['username']
        address = req['email']
        number = req['phone']
        password = req['password']
        confirmPassword = req['confirmPassword']

        if models.User.query.filter_by(username= uName):
            print('User account cretated successfully')


        user = models.User(
        firstName=fName, lastName=lName, username=uName, email=address, phone=number)

        user.set_password(password)
        db.session.add(user)
        db.session.commit()    
    
        print(fName, lName, uName, address, number, password, confirmPassword)
        message = "Account with username " + uName + " created"
        return redirect('/userLogin')
        

    return render_template('auth/signUp.html')

@app.route('/eBuy/aboutUs')
def aboutUs():
    return render_template('aboutUs.html')

@app.route('/eBuy/contactUs')
def contactUs():
    return render_template('contactUs.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')
