#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#Variant_1

class Time:
    def __init__(self):
        self.sec = None
        self.min = None
        self.hour = None

    def time_set(self):
        print("What time is it?")
        self.sec = int(input('How many seconds?: '))
        self.min = int(input('How many mins?: '))
        self.hour = int(input('How many hours?: '))

    def time_print(self):
        print(f"\nTime right now:\n{self.hour} : {self.min} : {self.sec}")


a = Time()
a.time_set()
a.time_print()
