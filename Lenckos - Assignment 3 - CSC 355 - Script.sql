/*
Michael Lenckos
CSC 355 Section 501
Assignment 3
1/29/2020
*/

-- 1. Give an alphabetical list of all cities that have at least one customer in them.
select distinct city from customer
ORDER BY city ASC;
-- 2. List the tiles and prices of all DVDs, from the least expensive to the most expensive.
select TITLE, TYPE, PRICE from  ITEM
where type = 'DVD'
ORDER BY price ASC;
-- 3. Give the title, type, and price for all items that cost less than fifteen dollars, listed from the highestpriced
-- item to the lowest-priced item.
select title, type, price from item
where price < 15
order by price DESC;
-- 4. Give an alphabetical list of titles of all items that contain the word ‘West’ anywhere in the title.
select title from item where title like '%West%';
-- 5. List, in ascending order, the ID of every customer who placed at least one order during 2019.
select CUSTOMER.ID
from CUSTOMER
inner join purchase on customer.id = purchase.cid
where purchase.pdate >= '01-JAN-19' and purchase.pdate < '01-JAN-20'
order by customer.id asc;
-- 6. For each customer who has made at least one purchase, give the ID of the customer and the date of
-- their most recent purchase.
select CUSTOMER.ID, max(purchase.pdate)
from CUSTOMER
inner join purchase on customer.id = purchase.cid
group by customer.id;
-- 7. For each different type of item, give the type, and the price of the least expensive item of that type.
select item.type, min(price) 
from item
group by item.type;
-- 8. For each date on which at least one purchase was made, give the date and how many purchases were
-- made on that date, from date the most purchases were made to the date the fewest purchases were made.
select sum(quantity), pdate
from purchase
group by pdate
order by sum(quantity) desc;
-- 9. Give the purchase ID and purchase date for all purchases made by customers named ‘Reed’, ordered
-- by the purchase ID. (You will need more than one table to do this; start by finding the inner join of
-- CUSTOMER and PURCHASE.)
select purchase.pid, purchase.pdate
from purchase
inner join customer 
on customer.id = purchase.cid
where customer.name = 'Reed'
order by purchase.pid;
-- 10. For each purchase, give the purchase ID and the total cost of that purchase (quantity times the price
-- of the purchased item), ordered from the highest total cost to the lowest. (Again, you will need more
-- than one table to do this; start by finding the inner join of PURCHASE and ITEM.)
select purchase.pid, purchase.quantity * item.price
from purchase
inner join item
on purchase.iid = item.id
order by purchase.quantity * item.price desc;