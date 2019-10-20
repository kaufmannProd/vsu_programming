#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def find_Season(n):
    season = {2 < n < 6: 'Весна', 5 < n < 9: 'Лето', 8 < n < 12: 'Осень', n < 3 or n == 12: 'Зима',}
    return season[True]

query = int(input("Какой у тебя сейчас месяц по счету?: "))
print(f"{find_Season(query)}? - чотка!")