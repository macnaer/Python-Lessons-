import mysql.connector
import requests
if __name__ == "__main__":
    db_manager


class db_manager():

    def __init__(self, host, user, passwd, database, url):
        self.__host = host
        self.__user = user
        self.__passwd = passwd
        self.__database = database
        self.__URL = url
        self.__db = mysql.connector.connect(
            host=self.__host, user=self.__user, passwd=self.__passwd)
        self.__cursor = self.__db.cursor()

    def __del__(self):
        self.__db.close()

    def get_all_data(self):
        response = requests.get(self.__URL)
        return response.json()

    def save_all_data(self, data):
        # print("save_all_data => ", data)
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS COVID_19;")
        self.__cursor.execute("USE COVID_19;")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS COVID_TABLE (id INT AUTO_INCREMENT PRIMARY KEY, country VARCHAR(255), countryCode VARCHAR(255), Slug VARCHAR(255), NewConfirmed INT(10),TotalConfirmed INT(10),NewDeaths INT(10),TotalDeaths INT(10),NewRecovered INT(10),TotalRecovered INT(10), Date DATETIME)")

        for item in data['Countries']:
            Country = item['Country']
            CountryCode = item['CountryCode']
            Slug = item['Slug']
            NewConfirmed = item['NewConfirmed']
            TotalConfirmed = item['TotalConfirmed']
            NewDeaths = item['NewDeaths']
            TotalDeaths = item['TotalDeaths']
            NewRecovered = item['NewRecovered']
            TotalRecovered = item['TotalRecovered']
            Date = item['Date']
            sql = "INSERT INTO COVID_TABLE (country,countryCode,Slug,NewConfirmed, TotalConfirmed, NewDeaths,TotalDeaths, NewRecovered, TotalRecovered, Date) VALUES (%s,%s,%s,%s,%s, %s, %s, %s, %s,%s)"
            val = (Country, CountryCode, Slug, NewConfirmed,
                   TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date)
            self.__cursor.execute(sql, val)
            self.__db.commit()
            print(self.__cursor.rowcount, "Country added")
