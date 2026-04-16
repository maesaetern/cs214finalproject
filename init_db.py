
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
            FOREIGN KEY (game_id) REFERENCES game (game_id)
        );
        
        CREATE TABLE sale (
            sale_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            NA_Sales DECIMAL NOT NULL,
            EU_Sales DECIMAL NOT NULL,
            JP_Sales DECIMAL NOT NULL,
            Other_Sales DECIMAL NOT NULL,
            Global_Sales DECIMAL NOT NULL,
            FOREIGN KEY (game_id) REFERENCES game (game_id)
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
            
         CREATE TABLE rank_sale (
            sale_id INT NOT NULL,
            rank INT NOT NULL,
            PRIMARY KEY (sale_id, rank)   
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
            EU_sales = row["EU Sales"]
            JP_sales = row["JP Sales"]
            Other_sales = row["Other Sales"]
            Global_sales = row["Global Sales"]


            rows.append((rank, name, platform, year, genre, publisher, NA_sales, EU_sales, JP_sales, Other_sales, Global_sales))
    if not rows:
        return

    cur.executemany(
        "INSERT INTO rank (rank, game_id) VALUES (%s, %s)",
        "INSERT INTO game (game_id, name, platform, year, genre, publisher)",
        "INSERT INTO sales (NA_sales, EU_sales, JP_sales, Other_sales, Global_sales, game_id) VALUES (%s, %s, %s, %s, %s, %s)",
        "INSERT INTO game_sale (game_id, sale_id) VALUES (%s, %s)"
    )


    conn.commit()
