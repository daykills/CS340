-- Class: CS 340
-- Student: Cheng Ying Wu, Sijun Chen
-- Project Step 4 Draft Version: DML and DDL Queries

-- This .SQL file contains the Data Manipulation Queries
-- Follows the UI functions in our webpages


-- Invoices Page
-- Create a new invoice
INSERT INTO Invoices (recordDate, orderID, quantity, totalAmount, acctID) VALUES (:recordDate_Input, :orderID_Input, :quantity_Input, :totalAmount_Input, :acctID_Input);

-- Search by InvoiceID
SELECT * FROM Invoices WHERE id= :invoicesID_selected_from_Invoices_page;

-- Show Invoice Register List
SELECT * FROM Invoices;

-- Update Function in the Invoice Register List
UPDATE Invoices SET recordDate= :recordDate_Input, orderID= :orderID_Input, quantity= :quantity_Input, totalAmount= :totalAmount_Input, acctID= :acctID_Input WHERE id= :invoicesID_selected_from_Invoices_page;

-- Delete Function in the Invoice Register List
DELETE FROM Invoices WHERE id= :invoicesID_selected_from_Invoices_page;


-- Orders Page
-- Search Orders by ID or customerID
SELECT * FROM Orders WHERE id= :orderID_selected_from_Orders_page OR customerID= :customerID_selected_from_Orders_page;

-- Display all outputs
SELECT * FROM Orders;

-- Update Function
UPDATE Orders SET customerID= :customerID_Input, quantity= :quantity_Input, totalCost = :totalCost_Input, status= :status_Input, shipmentStatus= :shipmentStatus_Input WHERE id= :orderID_selected_from_Orders_page;

-- Delete Function
DELETE FROM Orders WHERE id= :orderID_selected_from_Orders_page;

-- Add New Orders
INSERT INTO Orders (customerID, quantity, totalCost) VALUES (:customerID_Input, :quantity_Input, :totalCost_Input);


-- Products Page
-- Create a new product
INSERT INTO Products (name, quantity, cost) VALUES (:name_Input, :quantity_Input, :cost_Input);

-- Search by ProductID
SELECT * FROM Products WHERE id= :productID_selected_from_Products_page;

-- Show Products List
SELECT * FROM Products;

-- Update Function in the Products List
UPDATE Products SET name= :name_Input, quantity= :quantity_Input, cost= :cost_Input WHERE id= :productID_selected_from_Products_page;

-- Delete Function in the Products List
DELETE FROM Products WHERE id= :productID_selected_from_Products_page;


-- Salespeople Page
-- Search Salespeople by ID or Name
SELECT * FROM Salespeople WHERE id= :staffID_selected_from_Salespeople_page OR name= :name_inputted_from_Salespeople_page;

-- Display all outputs
SELECT * FROM Salespeople;

-- Update Function
UPDATE Salespeople SET name= :name_Input, age= :age_Input, saleAmount = :saleAmount_Input WHERE id= :staffID_selected_from_Salespeople_page;

-- Delete Function
DELETE FROM Salespeople WHERE id= :staffID_selected_from_Salespeople_page;

-- Add New Salespeople
INSERT INTO Salespeople (name, age, saleAmount) VALUES (:name_Input, :age_Input, :saleAmount_Input);


-- Accountants Page
-- Add a new accountant
INSERT INTO Accountants (name, age) VALUES (:name_Input, :age_Input);

-- Show Accountant Register List
SELECT * FROM Accountants;

-- Update Function in the Accountant Register List
UPDATE Accountants SET name= :name_Input, age= :age_Input WHERE id= :acctID_selected_from_Accountants_page;

-- Delete Function in the Accountant Register List
DELETE FROM Accountants WHERE id= :acctID_selected_from_Accountants_page;


-- Customers Page
-- Search Customers by ID or Name
SELECT * FROM Customers WHERE id= :customerID_selected_from_Customers_page OR name= :name_inputted_from_Customers_page;

-- Display all outputs
SELECT * FROM Customers;

-- Update Function
UPDATE Customers SET name= :name_Input, address= :address_Input, email= :email_Input, phoneNumber= :phoneNumber_Input WHERE id= :staffID_selected_from_Salespeople_page;

-- Delete Function
DELETE FROM Customers WHERE id= :staffID_selected_from_Salespeople_page;

-- Add New Customers
INSERT INTO Customers (name, address, email, phoneNumber) VALUES (:name_Input, :address_Input, :email_Input, :phoneNumber_Input);


-- Salespeople_Customers Page
-- Search by date, staffID, or customerID
SELECT * FROM Salespeople_Customers WHERE saleDate= :date_selected_from_Salespeople_Customers_page OR staffID= :staffID_inputted_from_Salespeople_Customers_page OR customerID= :customerID_inputted_from_Salespeople_Customers_page;

-- Display all outputs
SELECT * FROM Salespeople_Customers;

-- Update Function
UPDATE Salespeople_Customers SET saleDate= :date_Input, staffID= :staffID_Input, customerID= :customerID_Input, sales= :sales_Input WHERE id= :ID_selected_from_Salespeople_Customers_page;

-- Delete Function
DELETE FROM Salespeople_Customers WHERE id= :ID_selected_from_Salespeople_Customers_page;

-- Add New Sales Record
INSERT INTO Salespeople_Customers (saleDate, staffID, customerID, sales) VALUES (:saleDate_Input, :staffID_Input, :customerID_Input, :sales_Input);

-- Check Salespeople Information (ID or Name)
SELECT id, name FROM Salespeople WHERE id= :staffID_selected_from_Salespeople_Customers_page OR name= :staffName_selected_from_Salespeople_Customers_page;

-- Check Customers Information (ID or Name)
SELECT id, name FROM Customers WHERE id= :customerID_selected_from_Salespeople_Customers_page OR name= :customerName_selected_from_Salespeople_Customers_page;


-- Orders_Products Page
-- Show all Orders
SELECT * FROM Orders;

-- Show all Products
SELECT * FROM Products;

-- Show all Orders_Products
SELECT * FROM Orders_Products;

-- Add New Record
INSERT INTO Orders_Products (orderID, itemID, quantity) VALUES (:orderID_Input, :itemID_Input, :quantity_Input);

-- Update Function
UPDATE Orders_Products SET orderID= :orderID_Input, itemID= :itemID_Input, quantity= :quantity_Input WHERE orderID= :orderID_selected_from_Orders_Products_page OR itemID= :itemID_inputted_from_Orders_Products_page;

-- Delete Function
DELETE FROM Orders_Products WHERE orderID= :orderID_selected_from_Orders_Products_page OR itemID= :itemID_inputted_from_Orders_Products_page;

-- Search by Orders or Products
SELECT * FROM Orders_Products WHERE orderID= :orderID_selected_from_Orders_Products_page OR itemID= :itemID_inputted_from_Orders_Products_page;
