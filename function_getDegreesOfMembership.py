#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getDegreesOfMembership(a , b , c , d , value): 
    if(a < 0 and b < 0 and c >= 0 and d >= 0):
        if value < c:
            return 1
        elif c <= value < d:
            return (d - value) / (d - c)
        else:
            return 0

    if a >= 0 and b >= 0 and c >= 0 and d >= 0:
        if value < a:
            return 0
        elif a <= value < b:
            return (value - a) / (b - a)
        elif b <= value < c:
            return 1
        elif c <= value < d:
            return (d - value) / (d - c)
        else:
            return 0

    if(a >= 0 and b >= 0 and c < 0 and d < 0):
        if value < a:
            return 0
        elif a <= value < b:
            return (value - a) / (b - a)
        else:
            return 1