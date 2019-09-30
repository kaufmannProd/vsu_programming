#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

# шуршим циферками
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

# вывод результата выражения, округленного до 2-х знаков после запятой
print("Длина вектора = {:.2f}".format(sqrt(x**2 + y**2 +z**2)))
