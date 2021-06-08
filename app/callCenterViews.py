from app import app, models, db
from flask import render_template, request, redirect, session
from flask_login import current_user, login_user, logout_user


@app.route('/callCenterStaff/login',  methods=['GET', 'POST'])
def callCenterStaffLogin():
    if current_user.is_authenticated:
            return redirect('/ccStaff/dashboard')

    if request.method == 'POST':
        req = request.form
        username = req['username']
        passwordHash = req['password']
        ccStaff = models.CallCenterStaff.query.filter_by(username=username).first()
        if ccStaff is not None and ccStaff.check_password(passwordHash):
            session['ccId'] = ccStaff.id
            login_user(ccStaff)            
            return redirect('/ccStaff/dashboard')

    return render_template('callCenter/callCenterStaffLogin.html')


@app.route('/ccStaff/SignUp', methods=['GET', 'POST'])
def ccStaffSignUp():
    if request.method == "POST":
        req = request.form
        fName = req['firstName']
        lName = req['lastName']
        uName = req['username']
        address = req['email']
        number = req['phone']
        password = req['password']
        confirmPassword = req['confirmPassword']

        if models.CallCenterStaff.query.filter_by(username=uName):
            print('User account cretated successfully')

        ccStaff = models.CallCenterStaff(
            firstName=fName, lastName=lName, username=uName, email=address, phone=number)

        ccStaff.set_password(password)
        db.session.add(ccStaff)
        db.session.commit()


        print(fName, lName, uName, address, number, password, confirmPassword)
        message = "Account with username " + uName + " created"
        return redirect('/callCenterStaff/login')

    return render_template('callCenter/ccSignUp.html')


@app.route('/ccStaff/dashboard')
def ccStaffDashboard():
    if 'id' in session:
        id = session['id']
    return render_template('callCenter/dashboard.html')


@app.route('/ccStaff/placeOrder', methods=['GET', 'POST'])
def placeOrder():
    if request.method == "POST":
        req = request.form
        fName = req['firstName']
        lName = req['lastName']
        phone = req['phone']
        productId = req['productId']
        amount = req['amount']

        if 'id' in session:
            id = session['id']
            session['productId'] = productId

        

    order = models.PhoneOrder(firstName=fName, lastName=lName, phone=phone, productId=productId, amount=amount, servedBy=id)
    db.session.add(order)
    db.session.commit()
    return render_template('callCenter/phoneOrders.html')

@app.route('/ccStaff/profile')
def ccStaffProfile():
    return render_template('callCenter/ccStaffProfile.html')

@app.route('/ccStaff/orders', methods=['GET', 'POST'])
def orders():
    if 'id' in session and 'productId' in session:
        id = session['id']
        productId = session['productId']
        

    return render_template('callCenter/phoneOrders.html',
    orders=models.PhoneOrder.query.filter_by(servedBy=id), 
    products = models.Product.query.filter_by(id=productId))

