#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# заготовка массива под циферки + просим первую
mas_N = []
str_OK = input("Введи че-нибудь приличное: ")

# обкашляем че он там написал и пихаем в массив
while str_OK:
	mas_N.append(str_OK)
	str_OK = input("Введи че-нибудь приличное: ")
	
print("Вот че ты наделал:\n", mas_N)
