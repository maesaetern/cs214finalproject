
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
        CREATE TABLE rank (
            rank INT SIGNED AUTO_INCREMENT PRIMARY KEY,
            game_id INT NOT NULL AUTO_INCREMENT FOREIGN KEY,

           
        );
        CREATE TABLE sales (
            sale_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            NA_Sales DECIMAL NOT NULL,
            EU_Sales DECIMAL NOT NULL,
            JP_Sales DECIMAL NOT NULL,
            Other_Sales DECIMAL NOT NULL,
            Global_Sales DECIMAL NOT NULL,
            FOREIGN KEY (rank) REFERENCES rank (rank)
            );
            
        CREATE TABLE game (
            game_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            platform VARCHAR(50) NOT NULL,
            year INT NOT NULL,
            genre VARCHAR(50) NOT NULL,
            publisher VARCHAR(50) NOT NUL
            
        );
        CREATE TABLE game_sale (
            game_id INT NOT NULL,
            sale_id INT NOT NULL,
            PRIMARY KEY (game_id, sale_id)
            );
            
        
    """)



def populate_tables(conn, cur, csvfile):
    rows = []
    with open(csvfile, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rank = row["Rank"]
            name = row["Name"]
            platform = row["Platform"]
            year = int(row["Year"])
            genre = row["Genre"]
            publisher = row["Publisher"]
            NA_sales = row["NA Sales"]


            rows.append((rank, name, platform, year, genre, publisher))
    if not rows:
        return

    cur.executemany(
        "INSERT INTO videogame (rank, name, platform, year, genre, publisher) VALUES (%s, %s, %s, %s, %s)",
        rows
    )

    conn.commit()
