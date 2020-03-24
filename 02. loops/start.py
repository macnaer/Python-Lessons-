import random
# exit = True
# while exit:
#     a = int(input("0. Exit "))
#     if a == 0:
#         exit = False


# a = int(input("Enter digit: "))
# i = 1
# factorial = 1
# while i < a:
#     factorial *= i
#     i += 1

# print("Факторіал числа", a, " = ", factorial)

# count = 10

# for i in range(1, count):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")

days = 0
counter = 0

while days <= 7:
    #a = int(input("Temp = "))
    a = random.randrange(-50, 50)
    print("random number => ", a)
    if a > 10:
        counter += 1
    days += 1
print(counter)
