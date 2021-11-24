'''
select * from COMPANY;

CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER);

DROP TABLE shopping;

ALTER table shopping RENAME to shopp;

INSERT INTO shopping VALUES (1, 'Avokado', 5);
INSERT INTO shopping VALUES (2, 'Milk', 2);
INSERT INTO shopping VALUES (3, 'Bread', 3);
INSERT INTO shopping VALUES (4, 'Chocolate', 8);
INSERT INTO shopping VALUES (5, 'Bamba', 5);
INSERT INTO shopping VALUES (6, 'Orange', 10);

select * from shopping;

SELECT id, name FROM shopping;
SELECT * FROM shopping WHERE amount > 5;
SELECT * FROM shopping WHERE amount = 2;
SELECT * FROM shopping WHERE name LIKE 'Bamba';

DELETE from shopping WHERE name like 'Orange';

UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba';

UPDATE shopping SET amount=1 WHERE name LIKE 'Milk';

ALTER TABLE shopping ADD COLUMN maavar;

UPDATE shopping SET maavar=6 WHERE id=1;
UPDATE shopping SET maavar=3 WHERE id=2;
UPDATE shopping SET maavar=12 WHERE id=3;
UPDATE shopping SET maavar=8 WHERE id=4;
UPDATE shopping SET maavar=5 WHERE id=5;

select * from shopping;

SELECT * FROM shopping WHERE amount > 1 AND maavar > 5;

SELECT * FROM shopping WHERE maavar BETWEEN 3 AND 5;

SELECT * FROM shopping ORDER BY maavar desc;

CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO books VALUES (1, 'SQL PROGRAMMING');
INSERT INTO books VALUES (2, 'CSHARP PROGRAMMING');
INSERT INTO books VALUES (3, 'PYTHON PROGRAMMING');
DELETE FROM books;

SELECT COUNT(*) from shopping;
SELECT MAX(amount) from shopping;
SELECT AVG(amount) from shopping;
SELECT MIN(amount) from shopping;

INSERT INTO shopping VALUES (6, 'Onions', 3, 6);
INSERT INTO shopping VALUES (7, 'Orio', 1, 8);
Select maavar, COUNT(*) as number_of_items  FROM shopping GROUP BY maavar;
Select MAX(amount), maavar FROM shopping GROUP BY maavar;
SELECT * from shopping order by maavar;

SELECT id AS "SECRET", name, amount, maavar FROM shopping;

Select maavar, COUNT(*) as number_of_items FROM shopping
where maavar between 8 and 12
GROUP BY maavar
HAVING number_of_items > 1;

SELECT * FROM shopping ORDER BY maavar asc;

CREATE TABLE viewers (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, theatre_number INTEGER);
INSERT INTO viewers VALUES (1, "Danny", 20, 1);
INSERT INTO viewers VALUES (2, "Boris", 29, 1);
INSERT INTO viewers VALUES (3, "Elad", 22, 2);
INSERT INTO viewers VALUES (4, "Yuval", 32, 2);
INSERT INTO viewers VALUES (5, "Racheli", 20, 3);
INSERT INTO viewers VALUES (6, "Liam", 18, 3);
INSERT INTO viewers VALUES (7, "itay", 35, 4);

select * from viewers;
select count(*) how_many_viewers, avg(age), theatre_number
from viewers
where age > 18
group by theatre_number
having count(*) > 1;

CREATE TABLE prices (id INTEGER PRIMARY KEY, price INTEGER);
INSERT INTO prices VALUES (1, 3);
INSERT INTO prices VALUES (2, 7);
INSERT INTO prices VALUES (3, 12);
INSERT INTO prices VALUES (4, 5);
INSERT INTO prices VALUES (5, 3);
INSERT INTO prices VALUES (6, 2);
INSERT INTO prices VALUES (7, 10);

SELECT s.id product_id, s.name, s.amount product_amount, maavar, p.price product_price FROM shopping s
    JOIN prices p ON s.maavar=p.id;

SELECT s.id, s.name, s.amount, s.maavar, p.price, s.amount * p.price AS "SECRET"
FROM shopping s JOIN prices p ON s.id=p.id;

SELECT s.id, s.name, s.amount, s.maavar, p.price FROM shopping s JOIN
prices p ON s.id=p.id WHERE p.price = (SELECT MAX(price) FROM prices)

CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount INTEGER);

CREATE TABLE shopping_location (id INTEGER PRIMARY KEY, name TEXT, maavar INTEGER);
drop table shopping_location;

INSERT INTO shopping_location(id, name, maavar)
select id, name, maavar * 2
from shopping
where amount > 1;

select * from shopping_location;

'''