#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque

def igra_Gavna(muha):
    return not len(muha) % 2 and muha[0] == "D"

def popavs(searchD, puple):
    mas = []
    while searchD:
        shitEater = searchD.popleft()
        if shitEater not in mas:
            if igra_Gavna(shitEater):
                return shitEater
            else:
                searchD += puple.get(shitEater, [])
            mas.append(shitEater)
    return False

names = {
    "Meme": ["Aa", "Bb"],
    "Aa": ["shkola_FU", "Dota_klass"],
    "Bb": ["soglasen", "stav_klas"],
    "Dota_klass": ["tasty", "meal"]
    }

mom = deque(names)
alive = popavs(mom, names)

if alive:
    print(f"{alive} давно мать по лесам не искал?")
else:
    print("Все в порядке, мать жива")
