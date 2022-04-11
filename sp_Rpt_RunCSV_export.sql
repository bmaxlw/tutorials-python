-- [08.04.2022]: Returns data for export
CREATE PROCEDURE sp_Rpt_RunCSV_export
    @OrderID INT = NULL,
    @Customer NVARCHAR(30) = NULL,
    @CustomerPhone NVARCHAR(10) = NULL,
    @CustomerEmail NVARCHAR(30) = NULL,
    @ProdQT INT = 0,
    @ProdQT2 INT = 999999,
    @ProdName NVARCHAR(30) = NULL,
    @CustomerCountry NVARCHAR(3) = NULL,
    @CustomerCity NVARCHAR(30) = NULL,
    @ShippingAddress NVARCHAR(100) = NULL,
    @OrderPrice NUMERIC(19, 2) = 0,
    @OrderPrice2 NUMERIC(19, 2) = 99999999999999999.99,
    @Supplier NVARCHAR(30) = NULL
AS
SELECT *
  FROM vw_Rpt_CSV_export
 WHERE (   OrderID       = @OrderID
      OR   @OrderID IS NULL)
   AND (   Customer      LIKE CONCAT('%', @Customer, '%')
      OR   @Customer IS NULL)
   AND (   CustomerPhone LIKE CONCAT('%', @CustomerPhone, '%')
      OR   @CustomerPhone IS NULL)
   AND (   CustomerEmail LIKE CONCAT('%', @CustomerEmail, '%')
      OR   @CustomerEmail IS NULL)
   AND (   (ProdQT       > @ProdQT)
     AND   (ProdQT       < @ProdQT2)
      OR   @ProdQT IS NULL
      OR   @ProdQT2 IS NULL)
   AND (   ProdName      LIKE CONCAT('%', @ProdName, '%')
      OR   @ProdName IS NULL)
   AND (   CustomerCountry LIKE CONCAT('%', @CustomerCountry, '%')
      OR   @CustomerCountry IS NULL)
   AND (   CustomerCity LIKE CONCAT('%', @CustomerCity, '%')
      OR   @CustomerCity IS NULL)
   AND (   ShippingAddress LIKE CONCAT('%', @ShippingAddress, '%')
      OR   @ShippingAddress IS NULL)
   AND (   (OrderPrice   > @OrderPrice)
     AND   (OrderPrice   < @OrderPrice2)
      OR   @OrderPrice IS NULL
      OR   @OrderPrice2 IS NULL)
   AND (   Supplier      LIKE CONCAT('%', @Supplier, '%')
      OR   @Supplier IS NULL);

EXEC sp_Rpt_RunCSV_export;

DROP PROC sp_Rpt_RunCSV_export;




