import mysql.connector
if __name__ == "__main__":
    connect_to_db,
    add_card


def connect_to_db():
    db = mysql.connector.connect(
        host="localhost", user="root", passwd="")
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS CardManager;")
    cursor.execute("USE CardManager;")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS CreditCard (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), surname VARCHAR(255), amount INT(10), currancy VARCHAR(255))")

    return db


def add_card(name, surname, amount, currancy):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO CreditCard (name, surname, amount, currancy ) VALUES (%s,%s,%s,%s)"
    val = (name, surname, amount, currancy)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "CARD added")
