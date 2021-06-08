from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager

db = SQLAlchemy()
login_manager = LoginManager()



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(60), index=True)
    lastName = db.Column(db.String(60), index=True)
    username = db.Column(db.String(60), index=True, unique=True)
    phone = db.Column(db.String(15), index=True, unique=True)
    email = db.Column(db.String(60), index=True, unique=True)
    passwordHash = db.Column(db.String(250))
    order = db.relationship('Order', backref='user', lazy=True)
    delivery = db.relationship('DeliveryDetails', backref='user', lazy=True)
    
    def set_password(self, password):
        self.passwordHash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordHash, password)

    def __repr__(self):
        return self.id

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Admin(UserMixin, db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(60), index=True)
    lastName = db.Column(db.String(60), index=True)
    username = db.Column(db.String(60), index=True, unique=True)
    phone = db.Column(db.String(15), index=True, unique=True)
    email = db.Column(db.String(60), index=True, unique=True)
    passwordHash = db.Column(db.String(250))

    def set_password(self, password):
        self.passwordHash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordHash, password)

    def __repr__(self):
        return self.id


@login_manager.user_loader
def load_user(id):
    return Admin.query.get(int(id))


class CallCenterStaff(UserMixin, db.Model):
    __tablename__ = 'callCenterStaff'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(60), index=True)
    lastName = db.Column(db.String(60), index=True)
    username = db.Column(db.String(60), index=True, unique=True)
    phone = db.Column(db.String(15), index=True, unique=True)
    email = db.Column(db.String(60), index=True, unique=True)
    passwordHash = db.Column(db.String(250))
    order = db.relationship('PhoneOrder', backref="callCenterStaff", lazy=True)

    def set_password(self, password):
        self.passwordHash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordHash, password)

    def __repr__(self):
        return self.id

@login_manager.user_loader
def load_user(id):
    return CallCenterStaff.query.get(int(id))

class CustomerServiceStaff(UserMixin, db.Model):
    __tablename__ = 'customerServiceStaff'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(60), index=True)
    lastName = db.Column(db.String(60), index=True)
    username = db.Column(db.String(60), index=True, unique=True)
    phone = db.Column(db.String(15), index=True, unique=True)
    email = db.Column(db.String(60), index=True, unique=True)
    passwordHash = db.Column(db.String(250))
    def set_password(self, password):
        self.passwordHash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordHash, password)

    def __repr__(self):
        return self.id


@login_manager.user_loader
def load_user(id):
    return CustomerServiceStaff.query.get(int(id))


class StockingClerk(UserMixin, db.Model):
    __tablename__ = 'stockingClerks'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(60), index=True)
    lastName = db.Column(db.String(60), index=True)
    username = db.Column(db.String(60), index=True, unique=True)
    phone = db.Column(db.String(15), index=True, unique=True)
    email = db.Column(db.String(60), index=True, unique=True)
    passwordHash = db.Column(db.String(250))

    def set_password(self, password):
        self.passwordHash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordHash, password)

    def __repr__(self):
        return self.id


@login_manager.user_loader
def load_user(id):
    return StockingClerk.query.get(int(id))


class Product(UserMixin, db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), index=True)
    name = db.Column(db.String(255), index=True, unique=True)
    price = db.Column(db.Integer, index=True)
    description = db.Column(db.String(255), index=True)
    image = db.Column(db.LargeBinary, nullable=False)
    renderedData = db.Column(db.Text, nullable=False)
    order = db.relationship('Order', backref='product', lazy=True)
    phoneOrder = db.relationship('PhoneOrder', backref='product', lazy=True)
    warehouseOrder = db.relationship('WarehouseOrder', backref='product', lazy=True)

    def __repr__(self):
        return self.id

@login_manager.user_loader
def load_user(id):
    return Product.query.get(int(id))


class Order(UserMixin, db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    amount = db.Column(db.Integer)
    name = db.Column(db.String(255), index=True)
    # trackNumber = db.Column(db.Integer, db.ForeignKey(
    #     'deliveryCompanies.id'), nullable=False)

    def __repr__(self):
        return self.id


@login_manager.user_loader
def load_user(id):
    return Order.query.get(int(id))


class UserInvoice(UserMixin, db.Model):
    __tablename__ = 'userInvoices'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    firstName = db.Column(db.String(255), index=True)
    lastName = db.Column(db.String(255), index=True)

    def __repr__(self):
        return self.id


@login_manager.user_loader
def load_user(id):
    return UserInvoice.query.get(int(id))


class PhoneOrder(UserMixin, db.Model):
    __tablename__ = 'phoneOrders'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(60), index=True)
    lastName = db.Column(db.String(60), index=True)
    phone = db.Column(db.String(12), index=True)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    amount = db.Column(db.Integer)
    servedBy = db.Column(db.Integer, db.ForeignKey('callCenterStaff.id'), nullable=False)
    # trackingNumber = db.Column(db.Integer, db.ForeignKey('deliveryCompanies.id'), nullable=False)

    def __repr__(self):
        return self.id


@login_manager.user_loader
def load_user(id):
    return PhoneOrder.query.get(int(id))

class Store(UserMixin, db.Model):
        __tablename__ = 'stores'
        id = db.Column(db.Integer, primary_key=True)
        location = db.Column(db.String(60), index=True)
        proMaxQuantity = db.Column(db.Integer, index=True)
        GalaxyQuantity = db.Column(db.Integer, index=True)
        TecnoQuantity = db.Column(db.Integer, index=True)
        SamsungTabQuantity = db.Column(db.Integer, index=True)
        NikonQuantity = db.Column(db.Integer, index=True)
        CanonQuantity = db.Column(db.Integer, index=True)
        LenovoQuantity = db.Column(db.Integer, index=True)
        AsusQuantity = db.Column(db.Integer, index=True)

@login_manager.user_loader
def load_user(id):
    return Store.query.get(int(id))

class Warehouse(UserMixin, db.Model):
    __tablename__ = 'warehouses'
    id = db.Column(db.Integer, primary_key=True)
    proMaxQuantity = db.Column(db.Integer, index=True)
    GalaxyQuantity = db.Column(db.Integer, index=True)
    TecnoQuantity = db.Column(db.Integer, index=True)
    SamsungTabQuantity = db.Column(db.Integer, index=True)
    NikonQuantity = db.Column(db.Integer, index=True)
    CanonQuantity = db.Column(db.Integer, index=True)
    LenovoQuantity = db.Column(db.Integer, index=True)
    AsusQuantity = db.Column(db.Integer, index=True)
    warehouseOrder = db.relationship('WarehouseOrder', backref='warehouses', lazy=True)

@login_manager.user_loader
def load_user(id):
    return Warehouse.query.get(int(id))


class WarehouseOrder(UserMixin, db.Model):
    __tablename__ = 'warehouseOrders'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    manufacturer = db.Column(db.String(60), index=True)
    productId = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    warehouse = db.Column(db.Integer, db.ForeignKey('warehouses.id'), nullable=False)

@login_manager.user_loader
def load_user(id):
    return WarehouseOrder.query.get(int(id))
    

class DeliveryDetails(db.Model):
    __tablename__ = 'deliveryDetails'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    firstName = db.Column(db.String(60), index=True)
    lastName = db.Column(db.String(60), index=True)
    deliveryLocation = db.Column(db.String(60), index=True)
    phoneNumber = db.Column(db.String(255), index=True)
    reportId = db.relationship('DeliveryReport', backref='delivery', lazy=True)


@login_manager.user_loader
def load_user(id):
    return DeliveryDetails.query.get(int(id))


class DeliveryReport(db.Model):
    __tablename__ = 'deliveryReports'
    id = db.Column(db.Integer, primary_key=True)
    trackingNumber = db.Column(db.String(60), index=True)
    location = db.Column(db.String(60), index=True)
    deliveryId = db.Column(db.Integer, db.ForeignKey('deliveryDetails.id'), nullable=False)

@login_manager.user_loader
def load_user(id):
    return DeliveryReport.query.get(int(id))

class DeliveryCompany(db.Model):
    __tablename__ = 'deliveryCompanies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), index=True)
    deliveryLocation = db.Column(db.String(60), index=True)
    deliveryStatus = db.Column(db.String(60), index=True)
    # phoneOrder = db.relationship('PhoneOrder', backref="delivery", lazy=True)
    # order = db.relationship('Order', backref="delivery", lazy=True)


@login_manager.user_loader
def load_user(id):
    return DeliveryCompany.query.get(int(id))
