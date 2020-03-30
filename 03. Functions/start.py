def start():
    print("Hello World")

# start()
# def sum(a, b):
#     return a + b
# res = sum(5, 3)
# print("Res => ", res)
# def display_info(name="Bill", age=60):
#     print("Name:", name, "Age:", age)
# display_info("Tom", 23)
# display_info()


# def sum(*params):
#     result = 0
#     for i in params:
#         result += i

#     return result


# res = sum(2, 2, 2, 5, 100)
# print(res)

# Написати функцію, яка отримує відстань, яку пробіг спортсмен
# та час пробігу і повертає швидкість спортсмена. Відстань та час
#  пробігу вводяться користувачем

time = int(input("Time: "))
distance = int(input("Distance: "))


def find_speed(time, distance):
    sec = distance / time
    return sec * 60


result = find_speed(time, distance)
print("Speed = ", result)
