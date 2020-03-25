import copy
import random

# num = [5, 6, "Seven", 8, 7, True, [1, 55, 100500]]   # List

# # print(num)
# for item in num:
#     print(item)

# num[3] = 73
# num[6][1] = "Середа"
# num.append(42)
# num.insert(2, "Heare")
# num.remove(True)

# # num.sort()
# print("================================================>")

# for item in num:
#     print(item)

# print("List length => ", len(num))
# # print("Min => ", min(num))

# ///////////////////////////

person = ["Tom", "Bob", "Robert", "Tom"]

# for item in person:
#     print("User => ", item)

# print("#################After##################")
# person.pop()
# person.append("Alice")
# person.sort()
# print("Count => ", person.count("Tom"))

# for item in person:
#     print("User => ", item)

person.reverse()
# for item in person:
#     print("User => ", item)


# userDB = person

# for item in person:
#     print("person => ", item)

# for item in userDB:
#     print("userDB => ", item)

# userDB[0] = "Stiven"
# for item in person:
#     print("person => ", item)

# for item in userDB:
#     print("userDB => ", item)

# userDB = copy.deepcopy(person)

# userDB = person[0:2]
# # userDB[0] = "Stiven"
# for item in person:
#     print("person => ", item)

# for item in userDB:
#     print("userDB => ", item)


arr = []


def fill_arr(arr):
    i = 0
    while i < 7:
        arr.append(random.randint(-12, 50))
        i += 1


def show_arr(arr):
    for item in arr:
        print(item)


def find_plus_minus(arr):
    plus_numbers = 0
    minus_numbers = 0

    for item in arr:
        if item > 0:
            plus_numbers += 1
        elif item < 0:
            minus_numbers += 1
    print("plus_numbers = ", plus_numbers)
    print("minus_numbers = ", minus_numbers)


fill_arr(arr)
show_arr(arr)
find_plus_minus(arr)

# print(arr)
