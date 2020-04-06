class Person:
    def __init__(self, name, salary):
        # print("Constructor works")
        self.name = name
        self.salary = salary

    # def __del__(self):
    #     print("Destructor works")

    def show_person(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)


person1 = Person("Bill", 1500)
person1.show_person()

person2 = Person("Tom", 1500)
person2.show_person()


if person1.salary > person2.salary:
    print("Salary =", person1.name, " > ", person2.name)
elif person1.salary < person2.salary:
    print("Salary =", person1.name, " < ", person2.name)
else:
    print("Salary =", person1.name, " = ", person2.name)
