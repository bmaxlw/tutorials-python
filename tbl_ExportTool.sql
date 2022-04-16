CREATE TABLE Customers(
customer_id INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
customer_name NVARCHAR(30));

CREATE TABLE Representatives(
representative_id INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
representative_full_name NVARCHAR(100),
representative_phone NVARCHAR(10),
representative_email NVARCHAR(30));

CREATE TABLE CustomersInfo(
customer_info_id INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
customer_id INT NOT NULL,
customer_location_country NVARCHAR(3),
customer_location_city NVARCHAR(30),
customer_location_address NVARCHAR(100),
customer_location_phone NVARCHAR(10),
customer_location_email NVARCHAR(30),
customer_location_representative INT NOT NULL,
FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
FOREIGN KEY(customer_location_representative) REFERENCES Representatives(representative_id));

CREATE TABLE Products(
prod_id INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
prod_name NVARCHAR(30),
prod_price NUMERIC(19, 2),
prod_in_stock INT,
supplier INT NOT NULL,
FOREIGN KEY(supplier) REFERENCES Suppliers(supplier_id));

CREATE TABLE Suppliers(
supplier_id INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
supplier_name NVARCHAR(30),
supplier_phone NVARCHAR(10),
supplier_email NVARCHAR(30));

CREATE TABLE Orders(
order_id INT NOT NULL PRIMARY KEY IDENTITY(1, 1),
customer_id INT NOT NULL,
prod_id INT NOT NULL,
prod_qt INT,
order_price NUMERIC(19, 2),
FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
FOREIGN KEY(prod_id) REFERENCES Products(prod_id));