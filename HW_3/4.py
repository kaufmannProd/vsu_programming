#! /usr/bin/env python3
# -*- coding: utf-8 -*-

que = input("Введи че-нибудь: ")
cat = []

while que:
    cat.append(que)
    que = input("Введи еще че-нибудь: ")

print("Вот че получилось:\nЭлемент | Штук")
mn_cat = set(cat)
for x in mn_cat:
    print("{:^} {:^}шт.".format(x, cat.count(x)))