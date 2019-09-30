#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# ввод диапозона
fir = int(input("Введи первое число: "))
sec = int(input("Введи второе число: "))

# сумма кратных 5-ти
sum_N = 0

# считаем сумму
for i in range(fir, sec+1):
	if not i % 5:
		sum_N += i

print("Сумма чисел кратных 5-ти в заданном диапозоне =", sum_N)
