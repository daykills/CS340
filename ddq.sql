-- Class: CS 340
-- Student: Cheng Ying Wu, Sijun Chen
-- Project Step 4 Draft Version: DML and DDL Queries

-- a) Data Definition Queries
-- Customers
CREATE TABLE Customers (
  id INT(11) PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  phoneNumber INT(11) NOT NULL
);

-- Products
CREATE TABLE Products (
  id INT(11) PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  quantity INT(11) NOT NULL,
  cost DECIMAL(10, 2) NOT NULL
);

-- Orders
CREATE TABLE Orders (
  id INT(11) PRIMARY KEY AUTO_INCREMENT,
  customerID INT NOT NULL,
  quantity INT(11) NOT NULL,
  totalCost DECIMAL(10, 2) NOT NULL,
  status VARCHAR(255) NOT NULL,
  shipmentStatus VARCHAR(255) NOT NULL,
  FOREIGN KEY (customerID) REFERENCES Customers (id)
);

-- Accountants
CREATE TABLE Accountants (
  id INT(11) PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  age INT(11) NOT NULL
);

-- Invoices
CREATE TABLE Invoices (
  id INT(11) PRIMARY KEY AUTO_INCREMENT,
  recordDate DATE NOT NULL,
  orderID INT NOT NULL,
  quantity INT(11) NOT NULL,
  totalAmount DECIMAL(10, 2) NOT NULL,
  acctID INT NULL,
  FOREIGN KEY (orderID) REFERENCES Orders (id),
  FOREIGN KEY (acctID) REFERENCES Accountants (id)
);

-- Salespeople
CREATE TABLE Salespeople (
  id INT(11) PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  age INT(11) NOT NULL,
  saleAmount DECIMAL(10, 2) NOT NULL
);

-- Salespeople_Customers (M:M between Salespeople and Customers)
CREATE TABLE Salespeople_Customers (
  id INT(11) PRIMARY KEY AUTO_INCREMENT,
  saleDate DATE NOT NULL,
  staffID INT,
  customerID INT NOT NULL,
  sales DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (staffID) REFERENCES Salespeople (id),
  FOREIGN KEY (customerID) REFERENCES Customers (id)
);

-- Orders_Products (M:M between Orders and Products)
CREATE TABLE Orders_Products (
  id INT(11) PRIMARY KEY AUTO_INCREMENT,
  orderID INT NOT NULL,
  itemID INT NOT NULL,
  quantity INT(11) NOT NULL,
  FOREIGN KEY (orderID) REFERENCES Orders (id),
  FOREIGN KEY (itemID) REFERENCES Products (id)
);

-- Test that the tables were created
-- DESCRIBE Customers;
-- DESCRIBE Products;
-- DESCRIBE Invoices;
-- DESCRIBE Salespeople;
-- DESCRIBE Orders;
-- DESCRIBE Accountants;
-- DESCRIBE Salespeople_Customers;
-- DESCRIBE Orders_Products;


-- b) Sample Data
INSERT INTO Customers (name, address, email, phoneNumber) VALUES ("Sara Smith", "7581 Holly Ave. Bonita Springs, FL 34135", "smiths@hello.com", 7581341);
INSERT INTO Customers (name, address, email, phoneNumber) VALUES ("Miguel Cabrera", "7038 Branch Court Buffalo, NY 14215", "mc@hello.com", 7038142);
INSERT INTO Customers (name, address, email, phoneNumber) VALUES ("Bo Chan'g", "9478 Liberty Street Mobile, AL 36605", "bochang@hello.com", 9478366);

INSERT INTO Products (name, quantity, cost) VALUES ("iPhone 13", 300, 1500);
INSERT INTO Products (name, quantity, cost) VALUES ("Airpods Pro", 100, 200);
INSERT INTO Products (name, quantity, cost) VALUES ("Macbook Pro", 50, 2000);

INSERT INTO Orders (customerID, quantity, totalCost) VALUES (1, 2, 400);
INSERT INTO Orders (customerID, quantity, totalCost) VALUES (2, 4, 5200);
INSERT INTO Orders (customerID, quantity, totalCost) VALUES (3, 1, 2000);

INSERT INTO Accountants (name, age) VALUES ("Ananya Jaiswal", 35);

INSERT INTO Invoices (recordDate, orderID, quantity, totalAmount, acctID) VALUES ("2021-03-10", 1, 2, 400, 1);
INSERT INTO Invoices (recordDate, orderID, quantity, totalAmount, acctID) VALUES ("2021-03-12", 2, 2, 3000, 1);
INSERT INTO Invoices (recordDate, orderID, quantity, totalAmount, acctID) VALUES ("2021-03-15", 2, 1, 2000, 1);
INSERT INTO Invoices (recordDate, orderID, quantity, totalAmount, acctID) VALUES ("2021-03-16", 2, 1, 200, NULL);

INSERT INTO Salespeople (name, age, saleAmount) VALUES ("Michael Fern", 29, 2400);
INSERT INTO Salespeople (name, age, saleAmount) VALUES ("Abdul Rehman", 40, 5200);

INSERT INTO Salespeople_Customers (saleDate, staffID, customerID, sales) VALUES ("2021-03-08", 1, 1, 400);
INSERT INTO Salespeople_Customers (saleDate, staffID, customerID, sales) VALUES ("2021-03-10", 2, 2, 5200);
INSERT INTO Salespeople_Customers (saleDate, staffID, customerID, sales) VALUES ("2021-03-12", 1, 3, 2000);

INSERT INTO Orders_Products (orderID, itemID, quantity) VALUES (1, 2, 2);
INSERT INTO Orders_Products (orderID, itemID, quantity) VALUES (2, 1, 2);
INSERT INTO Orders_Products (orderID, itemID, quantity) VALUES (2, 2, 1);
INSERT INTO Orders_Products (orderID, itemID, quantity) VALUES (2, 3, 1);
INSERT INTO Orders_Products (orderID, itemID, quantity) VALUES (3, 3, 1);