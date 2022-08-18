import math

a, b, c = map(int, input().split())
if (a == 0):
    if (b != 0):
        print(-c / b)
    if (b == 0 and c == 0):
        print('Бесконечно кол-во решений')
else:
    d = b ** 2 - 4 * a * c
    if (d == 0):
        x1 = -b / 2 * a
        print(x1)
    elif (d > 0):
        x1 = (-b + d**0.5) / 2 * a
        x2 = (-b - d**0.5) / 2 * a
        print(x1, x2)
    else:
        print('Нет вещественных корней')
