from lib.db import add_capital


def menu():
    choice = int(input("1: Add capital"))
    if choice == 1:
        country = input("Country: ")
        capital = input("Capital: ")
        population = int(input("Population: "))
        mayor = input("Mayor: ")
        add_capital(country, capital, population, mayor)


menu()
