SELECT * FROM Album a;
SELECT COUNT(*) as Records FROM Album a;

SELECT COUNT(*) FROM Album a WHERE Column1 IS NOT NULL;
SELECT AlbumId, Title FROM Album a WHERE Column1 IS NULL;

SELECT * FROM Artist a;

--Caracterizando os registros dos artistas.
SELECT a2.ArtistId , a2.Name , COUNT(*) AS Records FROM Album a INNER JOIN Artist a2 GROUP BY 1;
SELECT a2.ArtistId , a2.Name , COUNT(*) AS Records FROM Album a INNER JOIN Artist a2 GROUP BY 1 ORDER BY Records DESC LIMIT 1;

SELECT * FROM Customer c LIMIT 10;
SELECT COUNT(*) FROM Customer c;
SELECT FirstName, Address FROM Customer c;
SELECT State, COUNT(*) AS Total FROM Customer c GROUP BY 1 ORDER BY Total DESC LIMIT 10;

--Quantos clientes moram na Broadway.
SELECT FirstName, COUNT(*) AS Total FROM Customer c WHERE Address LIKE '%Broadway';

--Verificar Company dos clientes.
SELECT COUNT(*) FROM Customer c WHERE Company IS NOT NULL;

SELECT FirstName FROM Customer c WHERE Company IS NULL;

SELECT * FROM Employee e;

SELECT * FROM Customer c ;

--Quais clientes são colaboradores. 
SELECT c.FirstName, c.LastName FROM Customer c WHERE Company IS NULL AND c.FirstName IN (SELECT e.FirstName FROM Employee e);

SELECT e.FirstName, c.LastName FROM Employee e INNER JOIN Customer c WHERE e.FirstName = c.FirstName ; 

SELECT e.FirstName FROM Customer c INNER JOIN Employee e WHERE c.Company IS NULL;


SELECT * FROM Invoice i LIMIT 10;
SELECT * FROM InvoiceLine il ORDER BY UnitPrice DESC LIMIT 10;

SELECT UnitPrice, COUNT(*) AS Record FROM InvoiceLine il GROUP BY UnitPrice;

--Clientes que possuem Invoice associados e a quantidade para cada cliente.
SELECT i.CustomerId, c.FirstName, COUNT(*) AS Record FROM InvoiceLine il INNER JOIN Invoice i INNER JOIN Customer c ON c.CustomerId = i.CustomerId GROUP BY i.CustomerId ORDER BY Record DESC;

--Verificando se existe redundância no retorno dos dados anteriores.
SELECT i.CustomerId, c.FirstName, COUNT(*) AS Record FROM Invoice i INNER JOIN Customer c ON c.CustomerId = i.CustomerId GROUP BY i.CustomerId ORDER BY Record DESC;

SELECT i.InvoiceId, il.InvoiceLineId FROM Invoice i INNER JOIN InvoiceLine il INNER JOIN Customer c ON c.CustomerId = i.CustomerId GROUP BY i.InvoiceId ORDER BY il.InvoiceLineId DESC LIMIT 100;








