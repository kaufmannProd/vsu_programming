#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def shellSort(mas):
    rast = len(mas) // 2

    while rast > 0:
        for startPos in range(rast):
            sortValue(mas, startPos, rast)

        print("После инкрементации размера на", rast,"массив:", mas)

        rast //= 2

def sortValue(mas, low, rast):
    
    for x in range(low + rast, len(mas), rast):
        currentvalue = mas[x]
        pos = x

        while pos >= rast and mas[pos - rast] > currentvalue:
            mas[pos] = mas[pos - rast]
            pos = pos - rast

        mas[pos] = currentvalue

from random import randint

is_mas = []

for x in range(20):
    is_mas.append(randint(0, 100))

print(f"Исходный массив:\n{is_mas}")

shellSort(is_mas)
