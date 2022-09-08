# Программа, которая высчитывает сумму всех цифр введенного вещественного числа

user_number = str(input("Введите вещественное число (дробную часть в случае ее наличия отделяйте запятой): "))

num_integer = True
sum = 0

for i in range(len(user_number)):
    if user_number[i] == ",":
        num_integer = False

if num_integer == True:
    new_number = int(user_number)
    while new_number > 0:
        sum = sum + int(new_number) % 10
        new_number = int(new_number) // 10
else:
    temp = user_number.split(",")
    left = int(temp[0])
    right = int(temp[1])

    while left > 0:
        sum = sum + left % 10
        left = left // 10

    while right > 0:
        sum = sum + right % 10
        right = right // 10

print(f"{user_number} -> {sum}")