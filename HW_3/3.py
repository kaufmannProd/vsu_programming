#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def fib_Seq(n):
    fib = [0, 1]
    for x in range(n - 2):
        fib.append(fib[-2] + fib[-1])
    return fib

que = int(input("Сколько чисел Фибоначчи показать?: "))
print(f"Забирай:\n{fib_Seq(que)}")