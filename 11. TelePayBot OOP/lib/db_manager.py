import mysql.connector
if __name__ == "__main__":
    db_manager


class db_manager():

    __db = ""

    def __init__(self, host, user, passwd, database="Test"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.__db = mysql.connector.connect(
            host=self.host, user=self.user, passwd=self.passwd)
        cursor = self.__db.cursor()

    def __del__(self):
        self.__db.close()
    # def connect_to_db():
    #     db = mysql.connector.connect(
    #         host="localhost", user="root", passwd="")
    #     cursor = db.cursor()
    #     cursor.execute("CREATE DATABASE IF NOT EXISTS CityBuilder;")
    #     cursor.execute("USE CityBuilder;")
    #     cursor.execute(
    #         "CREATE TABLE IF NOT EXISTS capitals (id INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(255), capital VARCHAR(255), population INT(10), mayor VARCHAR(255))")

    #     return db

    # def add_capital(country, capital, population, mayor):
    #     db = connect_to_db()
    #     cursor = db.cursor()
    #     sql = "INSERT INTO capitals (country,capital,population,mayor ) VALUES (%s,%s,%s,%s)"
    #     val = (country, capital, population, mayor)
    #     cursor.execute(sql, val)
    #     db.commit()
    #     print(cursor.rowcount, "Capital added")
