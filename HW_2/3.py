#! /usr/bin/env python3
# -*- coding: utf-8 -*-


# построение треугольника
def build_TR():
	
    # длина стороны?
    dlin = int(input("Введите длину стороны треугольника: "))
	
    # рисуем
    for i in range(dlin):
	print(" " * (dlin - i) + "*" * (i + 1) + "*" * i)

build_TR()
	

