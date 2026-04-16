import mysql.connector

class VideoGame:
    def __init__(self, rank, name,genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales):
        self.rank = rank
        self.name = name
        self.genre = genre
        self.publisher = publisher
        self.NA_sales = na_sales
        self.EU_sales = eu_sales
        self.JP_sales = jp_sales
        self.Other_sales = other_sales
        self.Global_sales = global_sales




class VideoGameDB:
    def __init__(self, host, username, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            username=username,
            password=password,
            database=database
        )

def disconnect(self):
    self.conn.close()

