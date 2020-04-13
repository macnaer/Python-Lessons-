import mysql.connector
import requests
if __name__ == "__main__":
    db_manager


class db_manager():
    __db = ""
    __cursor = ""

    def __init__(self, host, user, passwd, database, url):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.__URL = url
        self.__db = mysql.connector.connect(
            host=self.host, user=self.user, passwd=self.passwd)
        self.__cursor = self.__db.cursor()

    def __del__(self):
        self.__db.close()

    def get_all_data(self):
        response = requests.get(self.__URL)
        return response.json()

    def save_all_data(self, data):
        print("save_all_data => ", data)
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS COVID_19;")
        self.__cursor.execute("USE COVID_19;")

        #  cursor.execute( "CREATE TABLE IF NOT EXISTS capitals (id INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(255), capital VARCHAR(255), population INT(10), mayor VARCHAR(255))")

        # def add_capital(country, capital, population, mayor):
        #     db = connect_to_db()
        #     cursor = db.cursor()
        #     sql = "INSERT INTO capitals (country,capital,population,mayor ) VALUES (%s,%s,%s,%s)"
        #     val = (country, capital, population, mayor)
        #     cursor.execute(sql, val)
        #     db.commit()
        #     print(cursor.rowcount, "Capital added")
