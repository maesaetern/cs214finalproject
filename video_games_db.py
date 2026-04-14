class VideoGames:
    def __init__(self):
        Genre, Publisher, NA_Sales, EU_Sales, JP_Sales, Other_Sales, Global_Sales
        

import mysql.connector
class VideoGamesDB:
    def __init__(self, host, username, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            username=username,
            password=password,
            database=database
        )
