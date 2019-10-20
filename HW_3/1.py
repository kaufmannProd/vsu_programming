#! /usr/bin/env python3
# -*- coding: utf-8 -*-

u_str = "".join(input("Давай пример, порешаем: "))
symb = {"+", "-", "*", "**", "/", "//", "%"}
op = "".join(symb & set(u_str))
ind_op = u_str.find(op)
a = u_str[:ind_op]
b = u_str[ind_op + 1:]

if op in b:
    op *= 2
    b = u_str[ind_op + 2:]

a = float(a)
b = float(b)
symb = {"+": a + b, "-": a - b, "*": a * b, "**": a ** b, "/": a / b, "//": a // b, "%": a % b}
print(f"Вот че получилось: {symb[op]}")
