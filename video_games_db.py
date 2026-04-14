class VideoGames:
    def __init__(self):
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
