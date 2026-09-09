# -*- coding: cp1251 -*-
from mod1 import calculate_y
from mod2 import fib

print("1 — Обчислити вираз y = sqrt(x^2 + y^2)")
print("2 — Ряд Фібоначчі з 5-го по 25-й член")

choice = input("Оберіть пункт (1 або 2): ")

if choice == '1':
    x = float(input("Введіть x: "))
    y = float(input("Введіть y: "))
    print("Результат y =", calculate_y(x, y))

elif choice == '2':
    res, n = fib()
    print("Елементи ряду:", res)
    print("Кількість елементів:", n)

else:
    print("Невірний вибір")
