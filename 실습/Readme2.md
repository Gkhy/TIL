### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT * FROM playlist_track 'A'
order by 'playlistId' desc
limit 5;
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT * FROM tracks 'B'
order by 'playlistId'
limit 5;
``` 
 
### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql
SELECT PlaylistId,Name FROM playlist_track
JOIN tracks ON playlist_track.Trackid = tracks.Trackid
order by PlaylistId DESC LIMIT 10;
```  

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT PlaylistId,Name FROM tracks
join playlist_track on playlist_track.Trackid=tracks.Trackid
WHERE PlaylistId=10
Order by Name desc Limit 5 ;
``` 

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*) FROM tracks
Join artists On tracks.composer=artists.Name
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT COUNT(*) FROM tracks
LEFT JOIN artists ON tracks.Composer=artists.Name;
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
LEET JOIN의 경우ON뒤에 조건식에 들어맞지 않는 행들도 같이 포함되어서..
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT INvoiceLineId,InvoiceId FROM invoice_items order by InvoiceId LIMIT 5;

``` 

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceId,CustomerId FROM invoices
InvoiceId order by InvoiceId LIMIT 5;
``` 

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```
SELECT InvoiceLineId, invoices.InvoiceId FROM invoice_items Join invoices 
ON invoice_items.InvoiceId=invoices.InvoiceId
ORDER by invoices.InvoiceId DESC LIMIT 5;
``` 


### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```
SELECT InvoiceId,customers.CustomerId FROM invoices JOIN customers
ON customers.CustomerId=invoices.CustomerId
ORDER BY InvoiceId DESC LIMIT 5;

``` 

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```
SELECT invoice_items.InvoiceLineId,
invoice_items.InvoiceId,
customers.CustomerId
FROM invoice_items
JOIN invoices
ON invoice_items.InvoiceId=invoices.InvoiceId
Join customers
on invoices.CustomerId=customers.CustomerId
ORDER BY invoice_items.InvoiceId DESC
LIMIT 5;
```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT count(*) FROM invoices
JOIN invoice_items On invoice_items.InvoiceId=invoices.InvoiceId
JOIN customers ON invoices.CustomerId
=customers.CustomerId
GROUP BY customers.CustomerId
ORDER BY customers.CustomerId LIMIT 5;
```


