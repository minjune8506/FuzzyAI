#!/usr/bin/env python
# -*- coding: utf-8 -*-

from func_getDegreesOfMembership import getDegreesOfMembership

# a 와 b 사이의 접점 (value == 접점의 x 값) value = premise * b - premise * a + a
# c 와 d 사이의 접점 (value == 접점의 x 값) value = premise * c - premise * d + d
def very_low(premise):
    c = 5
    d = 20
    
    x1 = premise * c - premise * d + d
    div = float(2) # 실수형 나눗셈을 진행하기 위한 div

    return (premise * x1) + (((d - x1) * premise) / div)

def low(premise):
    a = 5
    b = 20
    c = 30
    d = 45

    x1 = premise * b - premise * a + a
    x2 = premise * c - premise * d + d
    div = float(2)

    return ((x1 - a) * premise / div) + ((x2 - x1) * premise) + ((d - x2) * premise / div)

def middle(premise):
    a = 30
    b = 45
    c = 55
    d = 70

    x1 = premise * b - premise * a + a
    x2 = premise * c - premise * d + d
    div = float(2)

    return ((x1 - a) * premise / div) + ((x2 - x1) * premise) + ((d - x2) * premise / div)

def high(premise):
    a = 55
    b = 70
    c = 80
    d = 95

    x1 = premise * b - premise * a + a
    x2 = premise * c - premise * d + d
    div = float(2)

    return ((x1 - a) * premise / div) + ((x2 - x1) * premise) + ((d - x2) * premise / div)


def very_high(premise):
    a = 80
    b = 95

    x1 = premise * b - premise * a + a
    div = float(2)

    return ((x1 - a) * premise / div) + ((100 - x1) * premise)

# premise = float(input())
# print("veryLow : " + str(very_low(premise)))
# print("low : " + str(low(premise)))
# print("middle : " + str(middle(premise)))
# print("high : " + str(high(premise)))
# print("veryhigh : " + str(very_high(premise)))
