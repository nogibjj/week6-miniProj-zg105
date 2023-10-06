[![CI](https://github.com/Jason-Guo1999/IDS706-Python-Template/actions/workflows/main.yml/badge.svg)](https://github.com/Jason-Guo1999/IDS706-Python-Template/actions/workflows/main.yml)
# IDS706-Week5-MiniProj
In this project, I use the Chinook_Sqltie sample database provided by https://https://github.com/lerocha/chinook-database. This query selects customer's information from the customers, albums, and artists tables.
```sql
SELECT
    c.FirstName || ' ' || c.LastName AS CustomerName,
    ar.Name AS ArtistName,
    al.Title AS AlbumTitle
FROM
    Customer c
JOIN
    Invoice i ON c.CustomerId = i.CustomerId
JOIN
    InvoiceLine il ON i.InvoiceId = il.InvoiceId
JOIN
    Track t ON il.TrackId = t.TrackId
JOIN
    Album al ON t.AlbumId = al.AlbumId
JOIN
    Artist ar ON al.ArtistId = ar.ArtistId
ORDER BY
    CustomerName;
```
### Query Explanation 
1. `SELECT c.FirstName || ' ' || c.LastName AS CustomerName, ar.Name AS ArtistName, al.Title AS AlbumTitle FROM Customer c`

      We are selecting the customer's name, artist name and album name from the "Customer" table.

2. `JOIN Invoice i ON c.CustomerId = i.CustomerId`

      We add invoice table, use customer id to join it with customer table.

3. `JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId`

      We add invoiceLine table, use invoice id to join it with invoice table.
    
4. `JOIN Track t ON il.TrackId = t.TrackId`

      We join Track table to find detailed information for customer's invoice.

5. `JOIN Album al ON t.AlbumId = al.AlbumId JOIN Artist ar ON al.ArtistId = ar.ArtistId`

      We add album and artist table to find artist name and album name.

6. `ORDER BY CustomerName`

      Sort the result in alphabetical order.

### Query Result
The quer yresult is stored in query_results.csv 