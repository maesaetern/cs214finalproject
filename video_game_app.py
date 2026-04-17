import os
from dotenv import load_dotenv

from video_games_db import VideoGame
from video_games_db import VideoGameDB
from init_db import setup_database

load_dotenv()


def main():
    setup_database("video_games_sales.csv")
    database = VideoGameDB(
        os.getenv("DBHOST"),
        os.getenv("USERNAME"),
        os.getenv("PASSWORD"),
        os.getenv("DATABASE")
    )

if __name__ == "__main__":
    main()
