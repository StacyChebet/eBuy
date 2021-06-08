from crypt import methods

from flask_sqlalchemy import _calling_context, model
from sqlalchemy.sql.expression import desc, true
from app import app
from flask import flash, render_template, request, redirect, session
from app import app
from app import models, db
from flask_login import current_user, login_user, logout_user
from base64 import b64encode
import base64
from sqlalchemy import func,desc
import sys
import numpy as np



def renderPicture(image):
    renderPic = base64.b64encode(image).decode('ascii')
    return renderPic

@app.route('/admin/SignUp', methods=['GET', 'POST'])
def adminSignUp():
    if request.method == "POST":
        req = request.form
        fName = req['firstName']
        lName = req['lastName']
        uName = req['username']
        address = req['email']
        number = req['phone']
        password = req['password']
        confirmPassword = req['confirmPassword']

        if models.Admin.query.filter_by(username=uName):
            print('User account cretated successfully')

        admin = models.Admin(
            firstName=fName, lastName=lName, username=uName, email=address, phone=number)

        admin.set_password(password)
        db.session.add(admin)
        db.session.commit()

        print(fName, lName, uName, address, number, password, confirmPassword)
        message = "Account with username " + uName + " created"
        return redirect('/admin/login')

    return render_template('admin/adminSignUp.html')


@app.route('/admin/login', methods=['GET', 'POST'])
def adminLogin():
    if current_user.is_authenticated:
        return redirect('/admin/dashboard')

    if request.method == 'POST':
        req = request.form
        username = req['username']
        passwordHash = req['password']
        admin = models.Admin.query.filter_by(username=username).first()
        if admin is not None and admin.check_password(passwordHash):
            login_user(admin)
            return redirect('/admin/dashboard')

    return render_template('admin/adminLogin.html')

@app.route('/admin/dashboard', methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        req = request.form
        productName = req['productName']
        category = req['category']
        price = req['price']
        description = req['description']
        image = request.files['image']
        imageData = image.read()
        renderFile = renderPicture(imageData)
        
        product = models.Product(category=category, name=productName, price=int(price), description=description, image=imageData, renderedData=renderFile)

       
        flash("Product " + productName + " added successfully")
    return render_template('admin/dashboard.html')


@app.route('/admin/products')
def productList():
    products = models.Product.query.all()    
    
    return render_template('admin/productList.html', products=products)


@app.route('/admin/users')
def userList():
    users = models.User.query.all()
    return render_template('admin/userList.html', users=users)


@app.route('/admin/ccStaff')
def ccList():
    cc = models.CallCenterStaff.query.all()
    return render_template('admin/ccStaff.html', cc=cc)


@app.route('/admin/csStaff')
def csList():
    cs = models.CustomerServiceStaff.query.all()
    return render_template('admin/csStaff.html', cs=cs)


@app.route('/admin/warehouseStaff')
def wStaffList():
    ss = models.StockingClerk.query.all()
    return render_template('admin/wStaff.html', ss=ss)


@app.route('/admin/topCustomer', methods=['GET', 'POST'])
def topCustomer():
    id = 1
    amount = 0
    highestId = db.session.query(func.max(models.Order.userId)).scalar()
    
    while id<=highestId:
        amount = db.session.query(func.sum(models.Order.amount)).filter(models.Order.userId == id).scalar()
        users = models.User.query.filter_by(id=id).all()
        for user in users:
            firstName = user.firstName
            lastName = user.lastName

        invoice = models.UserInvoice(userId=id, amount=amount, firstName=firstName, lastName=lastName)
        
        db.session.add(invoice)
        db.session.commit()
        id +=1

    inv = db.session.query(models.UserInvoice).order_by(desc(models.UserInvoice.amount)).limit(1)
    return render_template('admin/topCustomer.html', inv=inv)


@app.route('/admin/topProducts', methods=['GET', 'POST'])
def topProducts():
    productIds = []
    productCount = []
    productCountCopy = []
    proMax = models.Order.query.filter_by(productId=4).count()
    productCount.append(proMax)
    productIds.append(4)
    s20 = models.Order.query.filter_by(productId=2).count()
    (models.Order.productId==2)
    productCount.append(s20)
    productIds.append(2)
    nikon = models.Order.query.filter_by(productId=6).count()
    (models.Order.productId==6)
    productCount.append(nikon)
    productIds.append(6)
    canon = models.Order.query.filter_by(productId=5).count()
    (models.Order.productId==5)
    productCount.append(canon)
    productIds.append(5)
    lenovo = models.Order.query.filter_by(productId=7).count()
    (models.Order.productId==7)
    productCount.append(lenovo)
    productIds.append(7)
    asus = models.Order.query.filter_by(productId=10).count()
    (models.Order.productId==10)
    productCount.append(asus)
    productIds.append(10)
    tecno = models.Order.query.filter_by(productId=12).count()
    (models.Order.productId==12)
    productCount.append(tecno)
    productIds.append(12)
    samsungTab = models.Order.query.filter_by(productId=11).count()
    (models.Order.productId==11)
    productCount.append(samsungTab)
    productIds.append(11)

    for i in productCount:
        productCountCopy.append(i)
    productCountCopy.sort()
    maxValue = productCountCopy[7]
    maxValuePosition = productCount.index(maxValue)
    maxValueId = productIds[maxValuePosition]

    secondHighestCopy = productCountCopy[6]
    if secondHighestCopy==maxValue:
        secondHighestCopy=productCountCopy[5]
    elif secondHighestCopy==productCountCopy[5]:
        secondHighestCopy=productCountCopy[4]
    elif secondHighestCopy==productCountCopy[4]:
        secondHighestCopy=productCountCopy[3]
    elif secondHighestCopy==productCountCopy[3]:
        secondHighestCopy=productCountCopy[2]
    elif secondHighestCopy==productCountCopy[2]:
        secondHighestCopy=productCountCopy[1]
    elif secondHighestCopy==productCountCopy[1]:
        secondHighestCopy=productCountCopy[0]
        
    secondHighestPosition = productCount.index(secondHighestCopy)
    secondHighestId = productIds[secondHighestPosition]

    highestValue = models.Product.query.filter_by(id=maxValueId).first()
    secondHighestValue = models.Product.query.filter_by(id=secondHighestId).first()

    return render_template('admin/topProducts.html', highestValue=highestValue, 
    secondHighestValue=secondHighestValue, maxValue=maxValue, secondHighestCopy=secondHighestCopy)


@app.route('/admin/lateDelivery', methods=['GET', 'POST'])
def lateDelivery():
    return render_template('admin/latePackages.html')

@app.route('/LatePackages/Report', methods=['GET', 'POST'])
def latePackagesReport():
    if request.method == 'POST':
        req = request.form
        trackingNumber = req['trackingNumber']
        location = req['location']
        deliveryId = req['deliveryId']

        deliveryReport = models.DeliveryReport(trackingNumber=trackingNumber, location=location, deliveryId=deliveryId)
        db.session.add(deliveryReport)
        db.session.commit()

    lateDeliveries = models.DeliveryReport.query.all()

    return render_template('admin/latePackagesReport.html', lateDeliveries=lateDeliveries)

@app.route('/admin/outOfStock', methods=['GET', 'POST'])
def outOfStock():
    return render_template('admin/outOfStock.html')


