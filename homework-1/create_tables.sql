-- SQL-команды для создания таблиц
CREATE DATABASE north;

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100),
	birth_date date,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(100) UNIQUE,
	company_name text,
	contact_name varchar(100)
);

CREATE TABLE orders
(
	order_id int UNIQUE,
	customer_id varchar(100) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date date,
	ship_city varchar(100) NOT NULL
);

# Поочередно проверил в pg заполнение таблиц
SELECT * FROM employees
SELECT * FROM customers
SELECT * FROM orders