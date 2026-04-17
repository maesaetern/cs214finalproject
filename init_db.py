
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

    cur.execute("""
         CREATE TABLE game (
            game_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            platform VARCHAR(50) NOT NULL,
            year INT NOT NULL,
            genre VARCHAR(50) NOT NULL,
            publisher VARCHAR(50) NOT NUL
        )
        """)
    cur.execute("""
        CREATE TABLE rank (
            rank INT,
            game_id INT NOT NULL AUTO_INCREMENT FOREIGN KEY,
            PRIMARY KEY (rank)
            FOREIGN KEY (game_id) REFERENCES game (game_id)
        )
        """)
    cur.execute("""
        
        CREATE TABLE sale (
            sale_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            game_id INT NOT NULL,
            NA_Sales DECIMAL NOT NULL,
            EU_Sales DECIMAL NOT NULL,
            JP_Sales DECIMAL NOT NULL,
            Other_Sales DECIMAL NOT NULL,
            Global_Sales DECIMAL NOT NULL,
            FOREIGN KEY (game_id) REFERENCES game (game_id)
            )
            """)
    cur.execute("""
        
        CREATE TABLE game_sale (
            game_id INT NOT NULL,
            sale_id INT NOT NULL,
            PRIMARY KEY (game_id, sale_id)
        )
        """)
    cur.execute("""
            
         CREATE TABLE rank_sale (
            sale_id INT NOT NULL,
            rank INT NOT NULL,
            PRIMARY KEY (sale_id, rank)   
            )
            
    """)



def populate_tables(conn, cur, csvfile):
    games, ranks, sales = [], [], []
    with open(csvfile, "r") as f:
        reader = csv.DictReader(f)
        for game_id, row in enumerate(reader, start=1):
            games.append((game_id, row["Name"], row["Platform"], row["Year"], row["Genre"], row["Publisher"]))
        ranks.append((int(row["Rank"]), game_id))
        sales.append((
            game_id,
            row["NA_Sales"],
            row["EU_Sales"],
            row["JP_Sales"],
            row["Other_Sales"],
            row["Global_Sales"]
        ))
    if not games:
        return

    cur.executemany(
        "INSERT INTO game (game_id, name, platform, year, genre, publisher) VALUES (%s, %s, %s, %s, %s, %s)", games )
    cur.executemany(
        "INSERT INTO rank (rank, game_id) VALUES (%s, %s)", ranks )
    cur.executemany(
        "INSERT INTO sales (NA_sales, EU_sales, JP_sales, Other_sales, Global_sales, game_id) VALUES (%s, %s, %s, %s, %s, %s)",
        sales
    )


    conn.commit()
