class VideoGames:
    def __init__(self, Rank, Name,Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales):
        self.rank = Rank
        self.name = Name
        self.genre = Genre
        self.publisher = Publisher
        self.NA_sales = NA_Sales
        self.EU_sales = EU_Sales
        self.JP_sales = JP_Sales
        self.Other_sales = Other_Sales
        self.Global_sales = Global_Sales



import mysql.connector
class VideoGamesDB:
    def __init__(self, host, username, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            username=username,
            password=password,
            database=database
        )
