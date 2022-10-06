from config import db_user, db_pass, db_host, db
import mysql.connector

class db_cnx:
    
    def __init__(self):
        self.user = db_user
        self.password = db_pass
        self.host = db_host
        self.db = db
    
    def execute(self, query):
        cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.db)
        cursor = cnx.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cnx.close()
        return results

    def insert_one(self, sql, value):
        cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.db)
        cursor = cnx.cursor()
        cursor.execute(sql, value)
        cnx.commit()
        cnx.close()

    def insert_many(self, sql, values):
        cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.db)
        cursor = cnx.cursor()
        cursor.executemany(sql, value)
        cnx.commit()
        cnx.close()





