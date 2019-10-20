#! /usr/bin/env python3
# -*- coding: utf-8 -*-

spi = list(map(float, input("Введи числа: ")))
print(f"Среднее арифметическое твоих чисел = {sum(spi) / len(spi)}")