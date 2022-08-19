-- SQLite
-- SQLite
1. 모든 테이블의 이름을 출력하세요.
.tables

2. 모든 테이블의 데이터를 확인해보세요.
.schema album
.schema employees
.schema invoices
.schema playlists
.schema artists
.schema genres
.schema media_types
.schema tracks
.schema customers
.schema invoice_items
.schema playlist_track

3. 앨범(albums) 테이블의 데이터를 출력하세요.
SELECT * FROM albums;

4. 고객(customers) 테이블의 행 개수를 출력하세요.


5. 고객(customers) 테이블에서 고객이 사는 나라가 `USA`인 고객의 `FirstName`, `LastName`을 출력하세요.


6. 송장(invoices) 테이블에서 `BillingPostalCode`가 `NULL` 이 아닌 행의 개수를 출력하세요.


7. 송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력하세요.


8. 송장(invoices) 테이블에서 `InvoiceDate`의 년도가 `2013`인 행의 개수를 출력하세요.


9. 고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력하세요.


10. 고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.


11. 앨범(albums) 테이블에서 가장 많은 앨범이 있는 Artist의 `ArtistId`와 `앨범 수`를 출력하세요.


12. 앨범(albums) 테이블에서 보유 앨범 수가 10개 이상인 Artist의 `ArtistId`와 `앨범 수` 출력하세요


13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 와 `State`를 기준으로 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.


14.  고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.


15. 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력하세요.


16. 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력하세요.


17. 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력하세요.

