# Программа, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

user_number = int(input("Введите число: "))

user_list = list(range(1, user_number + 1))

for i in range(2, user_number):
    user_list[i] = user_list[i] * user_list[i - 1]

print(f"N = {user_number} -> {user_list}")