"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv


Password: str = os.getenv('pswd_pg')
conn = psycopg2.connect(host="localhost", database="north", user="postgres", password=Password)
try:
    with conn:
        with open('north_data\employees_data.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for line in reader:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO employees(employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)",
                                (line['employee_id'], line['first_name'], line['last_name'], line['title'], line['birth_date'], line['notes']))

        with open('north_data\customers_data.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for line in reader:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO customers(customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                                (line["customer_id"], line["company_name"], line["contact_name"]))

        with open('north_data\orders_data.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for line in reader:
                with conn.cursor() as cur:
                    cur.execute("INSERT INTO orders(order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)",
                                (line['order_id'], line['customer_id'], line['employee_id'], line['order_date'], line['ship_city']))

finally:
    conn.close()
