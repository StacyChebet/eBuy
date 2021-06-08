from crypt import methods
from app import app, models, db
from flask_login import current_user, login_user, logout_user
from flask import render_template, request, redirect
from app import app
from flask import render_template


@app.route('/warehouseStaff/login', methods=['GET', 'POST'])
def warehouseStaffLogin():
    if current_user.is_authenticated:
        return redirect('/warehouseStaff/dashboard')

    if request.method == 'POST':
        req = request.form
        username = req['username']
        passwordHash = req['password']
        warehouseStaff = models.StockingClerk.query.filter_by(
            username=username).first()
        if warehouseStaff is not None and warehouseStaff.check_password(passwordHash):
            login_user(warehouseStaff)
            return redirect('/warehouseStaff/dashboard')

    return render_template('warehouse/warehouseStaffLogin.html')

@app.route('/warehouseStaff/SignUp', methods=['GET', 'POST'])
def warehouseStaffSignUp():
    if request.method == "POST":
        req = request.form
        fName = req['firstName']
        lName = req['lastName']
        uName = req['username']
        address = req['email']
        number = req['phone']
        password = req['password']
        confirmPassword = req['confirmPassword']

        if models.StockingClerk.query.filter_by(username=uName):
            print('User account cretated successfully')

        warehouseStaff = models.StockingClerk(
            firstName=fName, lastName=lName, username=uName, email=address, phone=number)

        warehouseStaff.set_password(password)
        db.session.add(warehouseStaff)
        db.session.commit()

        print(fName, lName, uName, address, number, password, confirmPassword)
        message = "Account with username " + uName + " created"
        return redirect('/warehouseStaff/login')

    return render_template('warehouse/warehouseStaffSignUp.html')


@app.route('/warehouseStaff/dashboard')
def warehouseStaffStaffDashboard():
    return render_template('warehouse/dashboard.html')

@app.route('/warehouse/StoreOrders')
def storeOrders():
    return render_template('warehouse/storeOrders.html')

@app.route('/warehouse/warehouseOrders')
def warehouseOrders():
    return render_template('warehouse/warehouseOrders.html')

@app.route('/warehouse/PlaceOrder')
def placeWarehouseOrder():
    return render_template('warehouse/placeOrder.html')

@app.route('/warehouse/customerOrders')
def customerOrders():
    orders = models.Order.query.all()
    for order in orders:
        uId = order.userId
    
    return render_template('warehouse/customerOrders.html', 
    onlineOrders=models.Order.query.all(), 
    phoneOrders= models.PhoneOrder.query.all(),
    users = models.User.query.filter_by(id=uId).all())


@app.route('/warehouse/PhonesInventory', methods=['POST', 'GET'])
def phones():
    
    return render_template('warehouse/phonesInventory.html', phones=models.Warehouse.query.filter_by(id=1))


@app.route('/warehouse/TabletsInventory', methods=['POST', 'GET'])
def tablets():
    return render_template('warehouse/tabletsInventory.html', tablets=models.Warehouse.query.filter_by(id=1))


@app.route('/warehouse/CamerasInventory', methods=['POST', 'GET'])
def cameras():
    return render_template('warehouse/camerasInventory.html', cameras=models.Warehouse.query.filter_by(id=1))


@app.route('/warehouse/LaptopsInventory', methods=['POST', 'GET'])
def laptops():
    return render_template('warehouse/laptopsInventory.html', laptops=models.Warehouse.query.filter_by(id=1))


@app.route('/warehouse/updatePhones')
def updatePhones():
    return render_template('warehouse/updatePhones.html')


@app.route('/warehouse/updateTablets')
def updateTablets():
    return render_template('warehouse/updateTablets.html')


@app.route('/warehouse/updateCameras')
def updateCameras():
    return render_template('warehouse/updateCameras.html')


@app.route('/warehouse/updateLaptops')
def updateLaptops():
    return render_template('warehouse/updateLaptops.html')
