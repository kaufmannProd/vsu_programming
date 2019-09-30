#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# вариабле(2 шт.)
fir = float(input("Введите первое число: "))
sec = float(input("Введите второе число: "))

# сравнение значений переменных
if fir > sec:
    print("1-ое больше 2-го")
elif fir < sec:
    print("2-е больше 1-го")
else:
    print("Введенные числа равны")
