"""
This module provides funcitonality to connect to database
"""

from RPA.Database import Database

class DatabaseOperation:
    """Connects to a database"""

    def __init__(self) -> None:
        self.db = Database()
        try:
            self.db.connect_to_database(
                module_name='sqlite3',
                database='Tmdb.db')
        except Exception as e:
            print(f"The database connection error is: {str(e)}")


    def close_connection(self) -> None:
        """closes connection"""
        self.db.disconnect_from_database()

    def create_table(self) -> None:
        try:
            self.db.query("CREATE TABLE Movie(id INTEGER PRIMARY KEY AUTOINCREMENT, movie_name TEXT, audience_scores FLOAT, storyline TEXT, rating TEXT, genres TEXT, review_1 TEXT, review_2 TEXT, review_3 TEXT, review_4 TEXT, review_5 TEXT, status TEXT)")
        except Exception as e:
            print(f'Table creation error. {str(e)}')
        else:
            print("Table successfully created!")

    def insert_to_database(self, row) -> None:
        query = "INSERT INTO Movie(movie_name, audience_scores, storyline, rating, genres, review_1, review_2, review_3, review_4, review_5, status) VALUES(?,?,?,?,?,?,?,?,?,?,?);"
        try:
            self.db.query(query, data=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9], row[10]))
        except Exception as e:
            print(f"Error encountered! {str(e)}")
        else:
            print("Data record successfully stored into the database.")

