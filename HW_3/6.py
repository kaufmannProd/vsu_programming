#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

def num_Pr(n):
    for x in range(2, int(sqrt(n)) + 1):
        if not n % x:
            return False
    return True

num = int(input("Введи число: "))
num_id = {True: "простое", False: "сложнаааа"}
print(f"Твое число - {num_id[num_Pr(num)]}")