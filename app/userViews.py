from flask.helpers import flash
from jinja2 import utils
from sqlalchemy.sql.functions import func
from app import app, models, db
from flask_login import current_user, login_user, logout_user
from flask import render_template, request, redirect, session


@app.route('/userLogin', methods=['GET', 'POST'])
def userLogin():
    if current_user.is_authenticated:
        return redirect('/eBuy/Home')

    if request.method == 'POST':
        req = request.form
        username = req['username']
        passwordHash = req['password']
        user = models.User.query.filter_by(username = username).first()

        if user is not None and user.check_password(passwordHash):
            session['id'] = user.id
            session['username'] = user.username
            login_user(user)
            return redirect('/eBuy/Home')

    return render_template('user/userLogin.html')

@app.route('/user/Profile')
def userProfile():
    return render_template('user/userProfile')

@app.route('/eBuy/Home', methods=['GET', 'POST'])
def home():
    if 'id' in session and 'username' in session:
        id = session['id']
        username = session['username'] 

    return render_template(
        'user/home.html', products = models.Product.query.all())

@app.route('/Add/to/cart', methods=['GET', 'POST'])
def addToCart():
    if 'id' in session and 'username' in session:
        id = session['id']
        username = session['username']

    if request.method == 'POST':
        req = request.form
        productId = int(req['addId'])
        userId = int(req['userId'])
        amount = int(req['price'])

        product = models.Product.query.filter_by(id=productId).first()
        name = product.name

        session['pId'] = productId

    order = models.Order(userId=userId, productId=productId, amount=amount, name=name)
    db.session.add(order)
    db.session.commit()

    return redirect('/Cart')

@app.route('/Cart', methods=['GET', 'POST'])
def cart():
    if 'id' in session and 'username' in session:
        id = session['id']
        username = session['username']


    counter = 0

    orders = models.Order.query.filter_by(userId=id).all()
    
    for order in orders:
        if order not in orders:
            redirect('/Empty/Cart')

        session['orderId'] = order.id
        pId = order.productId
        
        
        counter += order.amount
    
    return render_template('user/cart.html', orders=orders, counter=counter)
    

@app.route('/Cart/Checkout', methods=['GET', 'POST'])
def checkOut():
    counter = 0
    if 'id' in session:
        id = session['id']
        orderId = session['orderId']
    if request.method == 'POST':
        req = request.form
        userId = req['userId']
    
        orders = models.Order.query.filter_by(userId=userId).all()
        
        for order in orders:
            counter += order.amount
        session['total'] = counter

    return render_template('user/checkout.html')

@app.route('/paymentMethods')
def paymentMethods():
    return render_template('user/paymentMethods.html')

@app.route('/user/logout')
def userLogout():
    logout_user()
    session.pop('userId', None)
    session.pop('Username', None)
    return redirect('/')


@app.route('/Delete/Item', methods=['GET', 'POST'])
def deleteItem():
    if 'id' in session:
        id = session['id']
        order = session['orderId']
    if request.method == 'POST':
        req = request.form
        orderId = int(req['deleteId'])

        deletedOrder = models.Order.query.filter_by(id=orderId).one()
        db.session.delete(deletedOrder)
        db.session.commit()

        flash('Order deleted successfully')
        return redirect('/Cart')

@app.route('/Delivery/details', methods=['GET', 'POST'])
def deliveryDetails():
    if 'id' in session:
        id = session['id']


    if request.method == 'POST':
        req = request.form
        userId = id
        location = req['location']
        firstName = req['firstName']
        lastName = req['lastName']
        phone = req['phone']

        details = models.DeliveryDetails(userId=userId, deliveryLocation=location, firstName=firstName, lastName=lastName, phoneNumber=phone)
        db.session.add(details)
        db.session.commit()

        flash("Delivery details submitted")
    
    return redirect('/Cart')
    
@app.route('/Delivery/Form', methods=['GET', 'POST'])
def delivery():
    if request.method == 'POST':
        if 'id' in session:
            id=session['id']
    return render_template('user/deliveryDetails.html')

@app.route('/Empty/Cart', methods=['GET', 'POST'])
def emptyCart():
    if 'id' in session:
        id = session['id']
    return render_template('user/emptyCart.html')

