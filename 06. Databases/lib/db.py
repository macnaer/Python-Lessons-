import mysql.connector
if __name__ == "__main__":
    connect_to_db,
    add_capital


def connect_to_db():
    db = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="countries")

    return db


def add_capital(country, capital, population, mayor):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO capitals (country,capital,population,mayor ) VALUES (%s,%s,%s,%s)"
    val = (country, capital, population, mayor)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "Capital added")
