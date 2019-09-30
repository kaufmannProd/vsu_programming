#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# рандом N, где a <= N <= b
from random import randint

game_num = randint(0,100)
u_num = int(input("Какое число загадаешь?: "))
u_trys = 0

# запускаем шарманку
while u_num != game_num:
	if u_num > game_num:
		print("Не угадал! Я загадал число поменьше))")
	if u_num < game_num:
		print("Не угадал! Я загадал число побольше))")
	u_num = int(input("Пробуй еще раз!: "))
	u_trys += 1
	
	
print("А почему рот в казино?! Красава, угадал. Тебе понадобилось целых {trys} попыток, чтобы угадать число {game}".format(trys = u_trys, game = game_num))
