from flask import Flask, render_template, json, redirect, url_for, session
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_chensij'
app.config['MYSQL_PASSWORD'] = '6547'
app.config['MYSQL_DB'] = 'cs340_chensij'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("home.html")

@app.route('/sql')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM actor''') 
    rv = cur.fetchall()
    return str(rv)

@app.route('/invoices')
def invoice():
    return render_template("invoice.html")
 

@app.route('/accountants')
def accountant():
    return render_template("accountant.html")

@app.route('/products')
def product():
    return render_template("product.html")

@app.route('/order_product')
def order_product():
    return render_template("order_product.html")

@app.route('/orders')
def order():
    return render_template("order.html")
 

@app.route('/customers')
def customer():
    return render_template("customer.html")

@app.route('/salespeople')
def salespeople():
    return render_template("salespeople.html")

@app.route('/sales_customer')
def sales_customer():
    return render_template("sales_customer.html")

if __name__ == "__main__":
    app.run(port=9112, debug=True) 
