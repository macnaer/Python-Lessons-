import mysql.connector
if __name__ == "__main__":
    add_capital


def connect_to_db():
    db = mysql.connector.connect(
        host="localhost", user="root", passwd="")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Currency;")
    cursor.execute("USE CityBuilder;")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS currency (id INT AUTO_INCREMENT PRIMARY KEY, ccy VARCHAR(255), base_ccy VARCHAR(255), buy FLOAT(10), sale FLOAT(10))")

    return db


def add_currency(ccy, base_ccy, buy, sale):
    print(ccy, " ", base_ccy, " ", buy, " ", sale)
