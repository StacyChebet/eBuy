from app import app
from flask import render_template

@app.route('/Cart')
def cart():
    return render_template('cart/cart.html')

@app.route('/paymentMethods')
def paymentMethods():
    return render_template('cart/paymentMethods.html')

@app.route('/previousPurchases')
def previousPurchases():
    return render_template('cart/previousPurchases.html')

