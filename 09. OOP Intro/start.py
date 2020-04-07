import random
from lib.db_manager import add_card
# class Person:
#     def __init__(self, name, salary):
#         # print("Constructor works")
#         self.name = name
#         self.salary = salary

#     # def __del__(self):
#     #     print("Destructor works")

#     def show_person(self):
#         print("Name: ", self.name)
#         print("Salary: ", self.salary)


# person1 = Person("Bill", 1500)
# person1.show_person()

# person2 = Person("Tom", 1500)
# person2.show_person()


# if person1.salary > person2.salary:
#     print("Salary =", person1.name, " > ", person2.name)
# elif person1.salary < person2.salary:
#     print("Salary =", person1.name, " < ", person2.name)
# else:
#     print("Salary =", person1.name, " = ", person2.name)

class Account:
    def __init__(self, number, name, surname, amount, currancy):
        self.name = name
        self.surname = surname
        self.number = number
        self.amount = amount
        self.currancy = currancy

    def show_account_info(self):
        print("Number => ",  self.number, "\nName => ", self.name, "\nSurname => ", self.surname,  "\nAmount => ",
              self.amount, "\nCurrency => ", self.currancy)

    def set_money(self, amount):
        print("Added money... ", amount, self.currancy)
        self.amount += amount

    def get_money(self, amount):
        print("Get money... ", amount, self.currancy)
        self.amount -= amount


card1 = Account(random.randint(1000000000000000,
                               9999999999999999), "Bill", "Gates", 1000, "UAH")


card1.show_account_info()
add_card(card1.name, card1.surname, card1.amount, card1.currancy)
# card1.set_money(30)
# card1.show_account_info()
# card1.get_money(240)
# card1.show_account_info()

# print("=====================================================")

# card2 = Account(random.randint(1000000000000000,
#                                9999999999999999), 3200, "UAH")
# card2.show_account_info()
# print("=====================================================")
# sum = 100
# card1.amount += sum
# card2.amount -= sum

# card1.show_account_info()
# card2.show_account_info()
