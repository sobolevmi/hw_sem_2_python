# Генератор случайных чисел

import datetime

start = int(input("Введите начало диапазона случайно генерируемых чисел: "))
end = int(input("Введите конец диапазона случайно генерируемых чисел: "))

if start != end:

    if start >= 0:

        if end >= 0 and end <= 10:
            dt = datetime.datetime.now()
            random = int(dt.microsecond) // 100000
            if random > end:
                random = start + 1

        if end >= 11 and end <= 100:
            dt = datetime.datetime.now()
            random = int(dt.microsecond) // 10000
            if random > end:
                random = start + 1

        if end >= 101 and end <= 1000:
            dt = datetime.datetime.now()
            random = int(dt.microsecond) // 1000
            if random > end:
                random = start + 1

        if end >= 1001 and end <= 10000:
            dt = datetime.datetime.now()
            random = int(dt.microsecond) // 100
            if random > end:
                random = start + 1

        if end >= 10001 and end <= 100000:
            dt = datetime.datetime.now()
            random = int(dt.microsecond) // 10
            if random > end:
                random = start + 1

        if end >= 100001 and end <= 1000000:
            dt = datetime.datetime.now()
            random = int(dt.microsecond)
            if random > end:
                random = start + 1

        if end > 1000000:
            dt = datetime.datetime.now()
            random = int(dt.microsecond) * 10
            if random > end:
                random = start + 1
    else:

        if end >= -10 and end <= -1:
            dt = datetime.datetime.now()
            random = int(dt.microsecond) // 100000
            random = -random
            if random < end:
                random = start - 1

    if end <= -11 and end >= -100:
        dt = datetime.datetime.now()
        random = int(dt.microsecond) // 10000
        random = -random
        if random < end:
            random = start - 1

    if end <= -101 and end >= -1000:
        dt = datetime.datetime.now()
        random = int(dt.microsecond) // 1000
        random = -random
        if random < end:
            random = start - 1

    if end <= -1001 and end >= -10000:
        dt = datetime.datetime.now()
        random = int(dt.microsecond) // 100
        random = -random
        if random < end:
            random = start - 1

    if end <= -10001 and end >= -100000:
        dt = datetime.datetime.now()
        random = int(dt.microsecond) // 10
        random = -random
        if random < end:
            random = start - 1

    if end <= -100001 and end >= -1000000:
        dt = datetime.datetime.now()
        random = int(dt.microsecond)
        random = -random
        if random < end:
            random = start - 1

    if end < -1000000:
        dt = datetime.datetime.now()
        random = int(dt.microsecond) * 10
        random = -random
        if random > end:
            random = start - 1

    print(f"Случайно сгенерированное число: {random}")

else:

    print("Числа не должны быть равны")