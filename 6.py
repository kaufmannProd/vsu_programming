#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# ввод циферок
num = float(input("Пошурши циферками: "))

# абонент - абонент?
if num.is_integer():
	print("Абонент - абонент")
else:
	print("Абонент - не абонент")
