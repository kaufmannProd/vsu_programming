#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# флот коорд
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

# в какой четверти
if x > 0 and y > 0:
    print("1-я четверть")
elif x < 0 and y > 0:
    print("2-я четверть")
elif x < 0 and y < 0:
    print("3-я четверть")
elif x > 0 and y < 0:
    print("4-я четверть")
elif not x and not y:
    print("Точка на оси -|-")
