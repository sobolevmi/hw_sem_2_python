# Программа по поиску палиндрома введенного числа

user_string_1 = str(input("Введите число: "))
user_string_2 = user_string_1[::-1]

if user_string_1 != user_string_2:
    while user_string_1 != user_string_2:
        result_1 = str(int(user_string_1) + int(user_string_2))
        result_2 = str(result_1[::-1])
        user_string_1 = result_1
        user_string_2 = result_2
    print(f"Палиндром введенного числа = {user_string_1}")
else:
    print("Введенное число уже является палиндромом")

