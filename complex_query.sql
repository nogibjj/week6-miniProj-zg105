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
