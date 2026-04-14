
import mysql.connector
import csv

import os

def setup_database(csvfile):
    create_database()
    with connect_db() as conn, conn.cursor() as cur:
        create_tables(cur)
        populate_tables(conn, cur, csvfile)

def connect_db():
    conn = mysql.connector.connect(
        host=os.getenv("DBHOST"),
        user=os.getenv("DBUSERNAME"),
        password=os.getenv("DBPASSWORD"),
        database=os.getenv("DATABASE")
    )
    return conn

def create_database():
    conn = mysql.connector.connect(
        host=os.getenv("DBHOST"),
        user=os.getenv("DBUSERNAME"),
        password=os.getenv("PASSWORD")
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"DROP DATABASE IF EXISTS {os.getenv('DATABASE')};")
    cursor.execute(f"CREATE DATABASE {os.getenv('DATABASE')};")
    cursor.close()
    conn.close()

def create_tables(cur):
    # Single table: dogs
    cur.execute("""
        CREATE TABLE dogs (
            id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            age TINYINT UNSIGNED NOT NULL,
            breed VARCHAR(100) NOT NULL
        );
    """)



def populate_tables(conn, cur, csvfile):
    row = []
    with open(csvfile, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rank = row["Rank"]
            name = row["Name"]
            platform = row["Platform"]
            year = row["Year"]
            genre = row["Genre"]
            publisher = row["Publisher"]
            Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales
