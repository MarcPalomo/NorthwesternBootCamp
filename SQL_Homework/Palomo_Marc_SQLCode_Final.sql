use sakila;
-- select * from actor;

-- 1a
select first_name, last_name from actor;

-- 1b
select CONCAT(UPPER(first_name), " ", UPPER(last_name)) as "Actor Name" 
from actor;

-- 2a
select actor_id, first_name, last_name from actor
where first_name = "Joe";

-- 2b
select actor_id, first_name, last_name from actor
where last_name LIKE '%gen%';

-- 2c
select actor_id, first_name, last_name from actor
where last_name LIKE '%LI%'
ORDER BY last_name, first_name;

-- 2d
select country_id, country from country
where country In
(select country from country
where country = "Afghanistan" or 
country = "Bangladesh" or 
country = "China");

-- 3a
alter table actor
add column description BLOB after last_name;

select * from actor;

-- 3b
alter table actor
drop column description;

select * from actor;

-- 4a
select last_name, count(last_name) from actor
group by last_name;

-- 4b
select last_name, count(last_name) from actor
group by last_name
having count(last_name) >= 2;

-- 4c
select actor_id, first_name, last_name from actor
where first_name = "Groucho" and last_name = "Williams";

Update actor SET first_name = "HARPO"
where first_name = "Groucho" and last_name = "Williams";

select * from actor
where first_name = "Harpo";

-- 4d
Update actor SET first_name = "Groucho"
where first_name = "Harpo";

-- 5a
show create table address;

-- CREATE TABLE `address` (
  -- `address_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  -- `address` varchar(50) NOT NULL,
  -- `address2` varchar(50) DEFAULT NULL,
  -- `district` varchar(20) NOT NULL,
  -- `city_id` smallint(5) unsigned NOT NULL,
  -- `postal_code` varchar(10) DEFAULT NULL,
  -- `phone` varchar(20) NOT NULL,
  -- `location` geometry NOT NULL,
  -- `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  -- PRIMARY KEY (`address_id`),
  -- KEY `idx_fk_city_id` (`city_id`),
  -- SPATIAL KEY `idx_location` (`location`),
  -- CONSTRAINT `fk_address_city` FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`) ON UPDATE CASCADE
-- ) ENGINE=InnoDB AUTO_INCREMENT=606 DEFAULT CHARSET=utf8

-- 6a (Incomplete address: only using tables 'staff' and 'address' per instructions)
select * from address;
select * from staff;

select staff.first_name, staff.last_name, address.address
from address
join staff on
staff.address_id = address.address_id;

-- 6b
select * from staff;
select * from payment;

select staff.staff_id, staff.first_name, staff.last_name, sum(payment.amount)
from staff
join payment on
staff.staff_id = payment.staff_id
where payment.payment_date between 
Cast('2005-08-01' AS Date) and Cast('2005-08-31' As Date)
group by staff.staff_id;

-- 6c
select * from film;
select * from film_actor;

select film.film_id, film.title, count(film_actor.actor_id)
from film
inner join film_actor on
film.film_id = film_actor.film_id
group by film_id;

-- 6d: There are 6 copies in the inventory system for "Hunchback Impossible".

select film.film_id, film.title, count(inventory.inventory_id)
from film
inner join inventory on
film.film_id = inventory.film_id
group by film_id
having film.title = "Hunchback Impossible";

-- checking work for 6d
-- select * from inventory
-- where film_id = 439;

-- 6e
select * from payment;
select * from customer;

select customer.first_name, customer.last_name, sum(payment.amount) as "Total Amount Paid"
from customer
join payment on
customer.customer_id = payment.customer_id
group by customer.customer_id
order by customer.last_name;

-- 7a
select title from film
where title LIKE 'K%' OR title LIKE 'Q%' and 
language_id in
(select language_id from language
where name = "English");

-- 7b

select first_name, last_name from actor
where actor_id in
(select actor_id
from film_actor
where film_id in
(select film_id
from film
where title = "Alone Trip"));

-- 7c
select * from customer;
select * from address;
select * from country;
select * from city;

select customer.first_name, customer.last_name, customer.email
from customer
inner join address on customer.address_id = address.address_id
inner join city on address.city_id = city.city_id
inner join country on city.country_id = country.country_id
where country = "Canada";

-- checking work
-- select first_name, last_name, email 
-- from customer
-- where address_id in
-- (select address_id
-- from address
-- where city_id in
-- (select city_id
-- from city
-- where country_id in
-- (select country_id
-- from country
-- where country = "Canada")));

-- 7d
select * from category;
select * from film;
select * from film_category;

select title from film
where film_id in
(select film_id
from film_category
where category_id in
(select category_id
from category
where name = "Family"));

-- 7e. Display the most frequently rented movies in descending order.
select * from rental;
select * from inventory;
select * from film;

select title, count(title) as "Count Rented"
from film
inner join inventory on film.film_id = inventory.film_id
right join rental on inventory.inventory_id = rental.inventory_id
group by title
order by count(title) desc;

-- 7f. Write a query to display how much business, in dollars, each store brought in.
select * from store;
select * from payment;
select * from staff;
select * from rental;

select staff.store_id, sum(payment.amount) as "Busines (in Dollars)"
from staff
join payment on staff.staff_id = payment.staff_id
group by staff.store_id;



-- 7g. Write a query to display for each store its store ID, city, and country.
select * from store;
select * from city;
select * from country;
select * from address;

select store.store_id, city.city, country.country
from store
inner join address on store.address_id = address.address_id
inner join city on address.city_id = city.city_id
inner join country on city.country_id = country.country_id;

-- 7h list the top 5 genres in gross revenue in descending order.
select * from category;
select * from film_category;
select * from inventory;
select * from payment;
select * from rental;

select category.name, sum(payment.amount)
from category
inner join film_category on category.category_id = film_category.category_id
inner join inventory on film_category.film_id = inventory.film_id
inner join rental on inventory.inventory_id = rental.inventory_id
inner join payment on rental.rental_id = payment.rental_id
group by category.name
order by sum(payment.amount) desc
limit 5;

-- 8a create a view of Top 5 genres by gross revenue (from 7h)
create view Top_5_Genres_GR as
select category.name, sum(payment.amount)
from category
inner join film_category on category.category_id = film_category.category_id
inner join inventory on film_category.film_id = inventory.film_id
inner join rental on inventory.inventory_id = rental.inventory_id
inner join payment on rental.rental_id = payment.rental_id
group by category.name
order by sum(payment.amount) desc
limit 5;

select * from Top_5_Genres_GR;

-- 8b How would you display the view that you create in 8a?
select * from Top_5_Genres_GR;

-- 8c Write a query to delete the above view.
drop view top_5_genres_gr;
-- Running the next line to check work and make sure it gets an error.
-- Also checking and refreshing the Schemas > Sakila > Views to make sure it disappears.
select * from top_5_genres_gr;