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

    def search_by_prefix(self, prefix, limit=10):
        # Search using LIKE
        sql = "SELECT game_id, name, platform, year, genre, publisher FROM game WHERE name LIKE %s ORDER BY game_id LIMIT %s"
        games = []
        with self.conn.cursor() as cur:
            cur.execute(sql, (prefix + "%", int(limit)))
            for r in cur.fetchall():
                games.append(VideoGame(r[1], r[2], r[3], r[4], r[5], r[6]))
        return games

    def get_video_game_by_name(self, name):
        sql = "SELECT game_id, name, platform, year, genre, publisher FROM games WHERE rank = %s"
        with self.conn.cursor(dictionary=True, buffered=True) as cur:
            cur.execute(sql, (name,))
            count = cur.rowcount
            games = [VideoGame(r['name'], r['platform']) for r in cur.fetchall()]
            return count, games

def disconnect(self):
    self.conn.close()

