class VideoGames:
    def __init__(self, Rank, Name, Platform, Year, Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales):
        self.Rank =  Rank
        self.Name = Name
        self.Platform = Platform
        self.Year = Year
        self.Genre = Genre
        self.Publisher = Publisher
        self.NA_sales = NA_Sales
        self.EU_sales = EU_Sales
        self.JP_Sales = JP_Sales
        self.Other_Sales = Other_Sales,
        self.Global_sales = Global_Sales
        pass

import mysql.connector
class VideoGamesDB:
    def __init__(self, host, username, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            username=username,
            password=password,
            database=database
        )
