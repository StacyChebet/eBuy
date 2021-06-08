from operator import methodcaller

from werkzeug.datastructures import ImmutableTypeConversionDict
from app import app, models, db
from flask import render_template, request, redirect
from flask_login import current_user, login_user, logout_user


@app.route('/customerServiceStaff/login', methods=['GET', 'POST'])
def customerServiceStaffLogin():
    
    if current_user.is_authenticated:
        return redirect('/csStaff/dashboard')

    if request.method == 'POST':
        req = request.form
        storeId = int(req['storeId'])
        username = req['username']
        passwordHash = req['password']
        csStaff = models.CustomerServiceStaff.query.filter_by(username=username).first()
        if csStaff is not None and csStaff.check_password(passwordHash):
            if storeId == 1:
                login_user(csStaff)
                return redirect('/csStaff/Town')
            elif storeId == 2:
                login_user(csStaff)
                return redirect('/csStaff/UpperHill')

    return render_template('customerService/customerServiceStaffLogin.html')


@app.route('/csStaff/SignUp', methods=['GET', 'POST'])
def csStaffSignUp():
    if request.method == "POST":
        req = request.form
        fName = req['firstName']
        lName = req['lastName']
        uName = req['username']
        address = req['email']
        number = req['phone']
        password = req['password']
        confirmPassword = req['confirmPassword']

        if models.CustomerServiceStaff.query.filter_by(username=uName):
            print('User account cretated successfully')

        csStaff = models.CustomerServiceStaff(
            firstName=fName, lastName=lName, username=uName, email=address, phone=number)

        csStaff.set_password(password)
        db.session.add(csStaff)
        db.session.commit()

        print(fName, lName, uName, address, number, password, confirmPassword)
        message = "Account with username " + uName + " created"
        return redirect('/customerServiceStaff/login')

    return render_template('customerService/csSignUp.html')

@app.route('/Town/Inventory', methods=['GET', 'POST'])
def townInventory():
    inventory = models.Store.query.filter_by(id=1).first()
    proMaxQuantity = inventory.proMaxQuantity
    GalaxyQuantity = inventory.GalaxyQuantity
    TecnoQuantity = inventory.TecnoQuantity
    SamsungTabQuantity = inventory.SamsungTabQuantity
    NikonQuantity = inventory.NikonQuantity
    CanonQuantity = inventory.CanonQuantity
    LenovoQuantity = inventory.LenovoQuantity
    AsusQuantity = inventory.AsusQuantity
    return render_template('customerService/townInventory.html', inventory=inventory)

@app.route('/UpperHill/Inventory')
def upperHillInventory():
    inventory = models.Store.query.filter_by(id=2).first()
    proMaxQuantity = inventory.proMaxQuantity
    GalaxyQuantity = inventory.GalaxyQuantity
    TecnoQuantity = inventory.TecnoQuantity
    SamsungTabQuantity = inventory.SamsungTabQuantity
    NikonQuantity = inventory.NikonQuantity
    CanonQuantity = inventory.CanonQuantity
    LenovoQuantity = inventory.LenovoQuantity
    AsusQuantity = inventory.AsusQuantity
    return render_template('customerService/upperHillInventory.html', inventory=inventory)

@app.route('/csStaff/Town')
def csStaffTownDashboard():
    return render_template('customerService/townDashboard.html')

@app.route('/csStaff/UpperHill')
def csStaffUpperHillDashboard():
    return render_template('customerService/upperHilldashboard.html')

