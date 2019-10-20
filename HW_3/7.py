#! /usr/bin/env python3
# -*- coding: utf-8 -*-

u_str = input("Давай побазарим:\n-").split()
dof = list(map(len, u_str))
print(f"\n{u_str[dof.index(max(dof))]} - О! А вы из англии?")

l_word = set(u_str)
dof = []
for x in l_word:
    dof.append(u_str.count(x))

print(f"Дофига {list(l_word)[dof.index(max(dof))]} базаришь - проще будь")