#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def u_Brackets(u_Str):
	
    # считаем скобочку
    BR_open = u_Str.count('(')
    BR_close = u_Str.count(')')
	
    # сколько не хватает?
    BR_dif = abs(BR_open - BR_close)
	
    # сморим каких не хватает
    if BR_open > BR_close:
	print("Не хватает {BR} - {SH} шт.".format(BR=")", SH=BR_dif))
	return 0
    elif BR_open < BR_close:
	print("Не хватает {BR} - {SH} шт.".format(BR = "(", SH = BR_dif))
	return 0
    print("Всего хватает, красава!")
    return

u_Str = input("Ну давай, пиши че ты там хотел. Скобок хватает? ")
u_Brackets(u_Str)
