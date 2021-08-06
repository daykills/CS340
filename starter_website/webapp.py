from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
webapp = Flask(__name__)

#provide a route where requests on the web application can be addressed
@webapp.route('/home')
def home():
    return render_template('index.html')

#read/search/add/edit/delete functions for 'Invoice' entity
@webapp.route('/invoice', methods=['POST','GET'])
def invoice():
    db_connection = connect_to_database()

    #search by invoiceID
    searchInvoiceID = request.args.get('searchInvoiceID')
    if searchInvoiceID:
        query = f"SELECT * FROM Invoices WHERE id = '{searchInvoiceID}'"
        result_search = execute_query(db_connection, query).fetchall()
        return render_template('invoice.html', rows=result_search)
    else:
        if request.method == 'POST':
            recordDate = request.form['recordDate']
            orderID = request.form['orderID']
            quantity = request.form['quantity']
            totalAmount = request.form['totalAmount']
            acctID = request.form['acctID']
            if not acctID:
                acctID = None
            query = 'INSERT INTO Invoices(recordDate, orderID, quantity, totalAmount, acctID) VALUES (%s,%s,%s,%s,%s)'
            data = (recordDate, orderID, quantity, totalAmount, acctID)
            execute_query(db_connection, query, data)
            
        orderID_query = 'SELECT id from Orders'
        orderID_results = execute_query(db_connection, orderID_query).fetchall()
        
        accountants_query = 'SELECT id, name from Accountants'
        accountants_results = execute_query(db_connection, accountants_query).fetchall()

        query = "SELECT * FROM Invoices"
        result = execute_query(db_connection, query).fetchall()
        return render_template('invoice.html', rows=result, orderIDs = orderID_results, accountants = accountants_results)

@webapp.route('/invoice_update/<int:pid>', methods=['POST', 'GET'])
def invoice_update(pid):
    db_connection = connect_to_database()

    if request.method == 'GET':
        invoice_query = 'SELECT * from Invoices WHERE id = %s' %(pid)
        invoice_result = execute_query(db_connection, invoice_query).fetchone()
        #fetchone: only return the first row
        accountants_query = 'SELECT id, name from Accountants'
        accountants_results = execute_query(db_connection, accountants_query).fetchall()

        return render_template('invoice_update.html', accountants = accountants_results, invoice = invoice_result)
        
    if request.method =='POST':
        recordDate = request.form['recordDate']
        orderID = request.form['orderID']
        quantity = request.form['quantity']
        totalAmount = request.form['totalAmount']
        acctID = request.form['acctID']
        
        update_query = f"UPDATE Invoices SET recordDate = %s, orderID = %s, quantity = %s, totalAmount = %s, acctID = %s WHERE id = '{pid}'"
        data = (recordDate, orderID, quantity, totalAmount, acctID)
        result = execute_query(db_connection, update_query, data)
   
        return redirect('/invoice')
     
@webapp.route('/invoice_delete/<int:id>')
def invoice_delete(id):
    '''deletes a invoice with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM Invoices WHERE id = %s"
    print(query)
    data = (id,)
    result = execute_query(db_connection, query, data)
    return redirect('invoice')
    

#read/search/add/edit/delete functions for 'Order' entity
@webapp.route('/order', methods=['POST','GET'])
def order():
    db_connection = connect_to_database()
    
    #search by orderID
    searchOrderID = request.args.get('searchOrderID')
    searchCustID = request.args.get('searchCustID')
    if searchOrderID or searchCustID:
        if searchOrderID:
            query = f"SELECT * FROM Orders WHERE id = '{searchOrderID}'"
        else:
            query = f"SELECT * FROM Orders WHERE customerID = '{searchCustID}'"

        result_search = execute_query(db_connection, query).fetchall()
        return render_template('order.html', rows=result_search)
    else:
        if request.method == 'POST':
            customerID = request.form['custID']
            quantity = request.form['quantity']
            totalCost = request.form['totalCost']
            status = request.form['status']
            shipmentStatus = request.form['shipmentStatus']
            
            query = 'INSERT INTO Orders(customerID, quantity, totalCost, status, shipmentStatus) VALUES (%s,%s,%s,%s,%s)'
            data = (customerID, quantity, totalCost, status, shipmentStatus)
            execute_query(db_connection, query, data)
            
        custID_query = 'SELECT id, name from Customers'
        custID_results = execute_query(db_connection, custID_query).fetchall()

        query = "SELECT * FROM Orders"
        result = execute_query(db_connection, query).fetchall()
        return render_template('order.html', rows=result, customers = custID_results)

@webapp.route('/order_update/<int:oid>', methods=['POST', 'GET'])
def order_update(oid):
    db_connection = connect_to_database()

    if request.method == 'GET':
        order_query = 'SELECT * from Orders WHERE id = %s' %(oid)
        order_result = execute_query(db_connection, order_query).fetchone()
        customers_query = 'SELECT id, name from Customers'
        customers_results = execute_query(db_connection, customers_query).fetchall()

        return render_template('order_update.html', customers = customers_results, order = order_result)
        
    if request.method =='POST':
        customerID = request.form['custID']
        quantity = request.form['quantity']
        totalCost = request.form['totalCost']
        status = request.form['status']
        shipmentStatus = request.form['shipmentStatus']

        update_query = f"UPDATE Orders SET customerID = %s, quantity = %s, totalCost = %s, status = %s, shipmentStatus = %s WHERE id = '{oid}'"
        data = (customerID, quantity, totalCost, status, shipmentStatus)
        result = execute_query(db_connection, update_query, data)
   
        return redirect('/order')

@webapp.route('/order_delete/<int:id>')
def order_delete(id):
    '''deletes a order with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM Orders WHERE id = %s"
    print(query)
    data = (id,)
    result = execute_query(db_connection, query, data)
    return redirect('order')

#read/search/add/edit/delete functions for 'Product' entity
@webapp.route('/product', methods=['POST','GET'])
def product():
    db_connection = connect_to_database()

    #search by productID
    searchProductID = request.args.get('searchProductID')
    if searchProductID:
        query = f"SELECT * FROM Products WHERE id = '{searchProductID}'"
        result_search = execute_query(db_connection, query).fetchall()
        return render_template('product.html', rows=result_search)
    else:
        if request.method == 'POST':
            name = request.form['name']
            quantity = request.form['quantity']
            cost = request.form['cost']
            query = 'INSERT INTO Products (name, quantity, cost) VALUES (%s,%s,%s)'
            data = (name, quantity, cost)
            execute_query(db_connection, query, data)
      
        query = "SELECT * FROM Products"
        result = execute_query(db_connection, query).fetchall()
        return render_template('product.html', rows=result)

@webapp.route('/product_update/<int:pid>', methods=['POST', 'GET'])
def product_update(pid):
    db_connection = connect_to_database()

    if request.method == 'GET':
        product_query = 'SELECT * from Products WHERE id = %s' %(pid)
        product_result = execute_query(db_connection, product_query).fetchone()
        return render_template('product_update.html',  product = product_result)
        
    if request.method =='POST':
        name = request.form['name']
        quantity = request.form['quantity']
        cost = request.form['cost']
        
        update_query = f"UPDATE Products SET name = %s, quantity = %s, cost = %s WHERE id = '{pid}'"
        data = (name, quantity, cost)
        result = execute_query(db_connection, update_query, data)
   
        return redirect('product')

@webapp.route('/product_delete/<int:id>')
def product_delete(id):
    '''deletes a product with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM Products WHERE id = %s"
    data = (id,)
    result = execute_query(db_connection, query, data)
    return redirect('product')
 
 #read/search/add/edit/delete functions for 'Salespeople' entity
@webapp.route('/salespeople', methods=['POST','GET'])
def salespeople():
    db_connection = connect_to_database()
    
    #search by salespeopleID
    searchSID = request.args.get('salespeopleID')
    searchName = request.args.get('searchName')
 
    if searchSID or searchName:
        if searchSID:
            query = f"SELECT * FROM Salespeople WHERE id = '{searchSID}'"
        else:
            query = f"SELECT * FROM Salespeople WHERE name LIKE '{searchName}' "
        result_search = execute_query(db_connection, query).fetchall()
        return render_template('salespeople.html', rows=result_search)
    else:
        if request.method == 'POST':
            name = request.form['staffName']
            age = request.form['age']
            saleAmount = request.form['saleAmount']
            query = 'INSERT INTO Salespeople (name, age, saleAmount) VALUES (%s,%s,%s)'
            data = (name, age, saleAmount)
            execute_query(db_connection, query, data)
            
        query = "SELECT * FROM Salespeople"
        result = execute_query(db_connection, query).fetchall()
        return render_template('salespeople.html', rows=result)
        
@webapp.route('/salespeople_update/<int:sid>', methods=['POST', 'GET'])
def salespeople_update(sid):
    db_connection = connect_to_database()

    if request.method == 'GET':
        salespeople_query = 'SELECT * from Salespeople WHERE id = %s' %(sid)
        salespeople_result = execute_query(db_connection, salespeople_query).fetchone()
        return render_template('salespeople_update.html',  salespeople = salespeople_result)
        
    if request.method =='POST':
        name = request.form['name']
        age = request.form['age']
        saleAmount = request.form['saleAmount']
        
        update_query = f"UPDATE Salespeople SET name = %s, age = %s, saleAmount = %s WHERE id = '{sid}'"
        data = (name, age, saleAmount)
        result = execute_query(db_connection, update_query, data)
   
        return redirect('salespeople')

@webapp.route('/salespeople_delete/<int:id>')
def salespeople_delete(id):
    '''deletes a salespeople with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM Salespeople WHERE id = %s"
    data = (id,)
    result = execute_query(db_connection, query, data)
    return redirect('salespeople')
  

 #read/add/edit/delete functions for 'Accountant' entity
@webapp.route('/accountant', methods=['POST','GET'])
def accountant():
    db_connection = connect_to_database()
    
    #add new accountant
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']

        query = 'INSERT INTO Accountants (name, age) VALUES (%s,%s)'
        data = (name, age)
        execute_query(db_connection, query, data)
        
    query = "SELECT * FROM Accountants"
    result = execute_query(db_connection, query).fetchall()
    return render_template('accountant.html', rows=result)

@webapp.route('/accountant_update/<int:aid>', methods=['POST', 'GET'])
def accountant_update(aid):
    db_connection = connect_to_database()

    if request.method == 'GET':
        accountant_query = 'SELECT * from Accountants WHERE id = %s' %(aid)
        accountant_result = execute_query(db_connection, accountant_query).fetchone()
        return render_template('accountant_update.html',  accountant = accountant_result)
        
    if request.method =='POST':
        name = request.form['name']
        age = request.form['age']
        
        update_query = f"UPDATE Accountants SET name = %s, age = %s WHERE id = '{aid}'"
        data = (name, age)
        result = execute_query(db_connection, update_query, data)
   
        return redirect('accountant')

@webapp.route('/accountant_delete/<int:id>')
def accountant_delete(id):
    '''deletes an accountant with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM Accountants WHERE id = %s"
    data = (id,)
    result = execute_query(db_connection, query, data)
    return redirect('accountant')

#read/search/add/edit/delete functions for 'Customer' entity
@webapp.route('/customer', methods=['POST','GET'])
def customer():
    db_connection = connect_to_database()
    
    #add new customer
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        email = request.form['email']
        phoneNumber = request.form['phoneNumber']

        query = 'INSERT INTO Customers(name, address, email, phoneNumber) VALUES (%s,%s,%s,%s)'
        data = (name, address, email, phoneNumber)
        execute_query(db_connection, query, data)
        
    query = "SELECT * FROM Customers"
    result = execute_query(db_connection, query).fetchall()
    return render_template('customer.html', rows=result)

@webapp.route('/customer_update/<int:cid>', methods=['POST', 'GET'])
def customer_update(cid):
    db_connection = connect_to_database()

    if request.method == 'GET':
        customer_query = 'SELECT * from Customers WHERE id = %s' %(cid)
        customer_result = execute_query(db_connection, customer_query).fetchone()
        return render_template('customer_update.html',  customer = customer_result)
        
    if request.method =='POST':
        name = request.form['name']
        address = request.form['address']
        email = request.form['email']
        phoneNumber = request.form['phoneNumber']
        
        update_query = f"UPDATE Customers SET name = %s, address = %s, email = %s, phoneNumber = %s WHERE id = '{cid}'"
        data = (name, address, email, phoneNumber)
        result = execute_query(db_connection, update_query, data)
   
        return redirect('customer')

@webapp.route('/customer_delete/<int:id>')
def customer_delete(id):
    '''deletes a customer with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM Customers WHERE id = %s"
    data = (id,)
    result = execute_query(db_connection, query, data)
    return redirect('customer')

#read/search/add/edit/delete functions for 'salespeople_customer' entity
@webapp.route('/sales_customer', methods=['POST','GET'])
def sales_customer():
    db_connection = connect_to_database()

    #Search by date, staffID, or customerID
    searchDate = request.args.get('searchDate')
    staff = request.args.get('staff')
    customer = request.args.get('customer')
    if searchDate or staff or customer:
        if searchDate:
            query = f"SELECT * FROM Salespeople_Customers WHERE saleDate = '{searchDate}'"
        elif staff:
            query = f"SELECT * FROM Salespeople_Customers WHERE staffID = '{staff}'"
        else:
            query = f"SELECT * FROM Salespeople_Customers WHERE customerID = '{customer}'"

        result_search = execute_query(db_connection, query).fetchall()
        return render_template('sales_customer.html', rows=result_search)

    #add new record
    if request.method == 'POST':
        saleDate = request.form['saleDate']
        staffID = request.form['staffID']
        customerID = request.form['customerID']
        sales = request.form['sales']

        query = 'INSERT INTO Salespeople_Customers(saleDate, staffID, customerID, sales) VALUES (%s,%s,%s,%s)'
        data = (saleDate, staffID, customerID, sales)
        execute_query(db_connection, query, data)
        

    salespeople_query = 'SELECT id, name from Salespeople'
    salespeople_results = execute_query(db_connection, salespeople_query).fetchall()
    
    customers_query = 'SELECT id, name from Customers'
    customers_results = execute_query(db_connection, customers_query).fetchall()

    query = "SELECT * FROM Salespeople_Customers"
    result = execute_query(db_connection, query).fetchall()
    return render_template('sales_customer.html', rows=result, staffIDs = salespeople_results, customers = customers_results)

@webapp.route('/sales_customer_update/<int:sid>', methods=['POST', 'GET'])
def sales_customer_update(sid):
    db_connection = connect_to_database()

    if request.method == 'GET':
        sales_customer_query = 'SELECT * from Salespeople_Customers WHERE id = %s' %(sid)
        sales_customer_result = execute_query(db_connection, sales_customer_query).fetchone()

        salespeople_query = 'SELECT id, name from Salespeople'
        salespeople_results = execute_query(db_connection, salespeople_query).fetchall()
        
        customers_query = 'SELECT id, name from Customers'
        customers_results = execute_query(db_connection, customers_query).fetchall()

        query = "SELECT * FROM Salespeople_Customers"
        result = execute_query(db_connection, query).fetchall()
 
        return render_template('sales_customer_update.html', staffIDs = salespeople_results, customers = customers_results, sp =sales_customer_result)
            
    if request.method =='POST':
        saleDate = request.form['saleDate']
        staffID = request.form['staffID']
        customerID = request.form['customerID']
        sales = request.form['sales']

        update_query = f"UPDATE Salespeople_Customers SET saleDate = %s, staffID = %s, customerID = %s, sales = %s WHERE id = '{sid}'"
        data = (saleDate, staffID, customerID, sales)
        result = execute_query(db_connection, update_query, data)
   
        return redirect('/sales_customer')

@webapp.route('/sales_customer_delete/<int:id>')
def sales_customer_delete(id):
    '''deletes a record with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM Salespeople_Customers WHERE id = %s"
    data = (id,)
    result = execute_query(db_connection, query, data)
    return redirect('sales_customer')

#read/search/add/edit/delete functions for 'order_product' entity
@webapp.route('/order_product', methods=['POST','GET'])
def order_product():
    db_connection = connect_to_database()

    #Search by Orders or Products
    search_orderID = request.args.get('search_orderID')
    search_itemID = request.args.get('search_itemID')
    if search_orderID or search_itemID:
        if search_orderID:
            query = f"SELECT * FROM Orders_Products WHERE orderID = '{search_orderID}'"
        else:
            query = f"SELECT * FROM Orders_Products WHERE itemID = '{search_itemID}'"
        result_search = execute_query(db_connection, query).fetchall()
        return render_template('order_product.html', rows=result_search)
    else:
        if request.method =='POST':
            orderID = request.form['orderID']
            itemID = request.form['itemID']
            quantity = request.form['quantity']

            query = 'INSERT INTO Orders_Products(orderID, itemID, quantity) VALUES (%s,%s,%s)'
            data = (orderID, itemID, quantity)
            execute_query(db_connection, query, data)
            
 
        order_product_query = "SELECT * FROM Orders_Products"
        op_result = execute_query(db_connection, order_product_query).fetchall()
        order_query = "SELECT * FROM Orders"
        order_result = execute_query(db_connection, order_query).fetchall()
        product_query = "SELECT * FROM Products"
        product_result = execute_query(db_connection, product_query).fetchall()
        return render_template('order_product.html', rows=op_result,order_rows=order_result, product_rows=product_result )
    
@webapp.route('/order_product_delete/<int:id>')
def order_product_delete(id):
    '''deletes a record with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM Orders_Products WHERE id = %s"
    data = (id,)
    result = execute_query(db_connection, query, data)
    return redirect('order_product')  
