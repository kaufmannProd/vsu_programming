#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Ввод строчки и искомой цифры
u_str = input("Введи строчку: ")
num = int(input("Какую цифру забыл?: "))

# достаем все циферки из строки
search_num = re.findall("\d", u_str)

print("Держи свою цифру - {}!".format(search_num[num - 1]))
