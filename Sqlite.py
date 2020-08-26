import sqlite3
from Logger import logger

class Sqlite:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
        except:
            logger.error('something wrong with reading db')

        return conn