SELECT * FROM Representatives;
SELECT * FROM Products; -- +
SELECT * FROM Suppliers; -- +
SELECT * FROM Customers; -- +
SELECT * FROM CustomersInfo; -- +
SELECT * FROM Orders; -- +

-- 1
INSERT INTO Customers(customer_name) VALUES('ADMK Kyiv Inc.');
INSERT INTO CustomersInfo(customer_id, customer_location_country, customer_location_city, customer_location_address, 
						  customer_location_phone, customer_location_email, customer_location_representative)
				   VALUES(4, 'UA', 'Kyiv', '5/115 Khreshchatyk Str.', '700500800', null, 1);
INSERT INTO Representatives(representative_full_name, representative_phone, representative_email)
					 VALUES('David Blackfield', '112448663', 'blackfield@jenkinsons.com');
INSERT INTO Products(prod_name, prod_price, prod_in_stock, supplier)
			  VALUES('Diesel Engine AD558996', 5999.99, 1100, 2);
INSERT INTO Suppliers(supplier_name, supplier_phone, supplier_email)
			VALUES('Maringthon Engines', '444788855', null);
INSERT INTO Orders(customer_id, prod_id, prod_qt, order_price, supplier)
			VALUES(4, 2, 120, 59999.00, 1);

CREATE VIEW vw_Rpt_CSV_export AS
SELECT 
OrderID         = od.order_id,
Customer        = cs.customer_name,
CustomerPhone   = csi.customer_location_phone,
CustomerEmail   = csi.customer_location_email,
ProdQT	        = od.prod_qt,
ProdName        = pr.prod_name,
CustomerCountry = csi.customer_location_country,
CustomerCity    = csi.customer_location_city,
ShippingAddress = CONCAT(csi.customer_location_address, ', ', csi.customer_location_city, ', ', csi.customer_location_country),
OrderPrice      = od.order_price,
Supplier        = sp.supplier_name
FROM 
Orders od INNER JOIN
Customers AS cs ON cs.customer_id = od.customer_id INNER JOIN
Products AS pr ON pr.prod_id = od.prod_id INNER JOIN
Suppliers AS sp ON sp.supplier_id = od.supplier INNER JOIN
CustomersInfo AS csi ON csi.customer_id = cs.customer_id;

SELECT * FROM vw_Rpt_CSV_export;
DROP VIEW vw_Rpt_CSV_export;

