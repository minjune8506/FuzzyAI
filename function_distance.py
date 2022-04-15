#!/usr/bin/env python
# -*- coding: utf-8 -*-

from function_getDegreesOfMembership import getDegreesOfMembership

def low(distance):
    return getDegreesOfMembership(-1 , -1 , 15 , 45 , distance)

def middle(distance):
    return getDegreesOfMembership(15 , 45 , 90 , 120 , distance)
        
def high(distance):
    return getDegreesOfMembership(90 , 120 , -1 , -1 , distance)

# distance = int(input())

# print("가까운 거리인 정도 : " + str(low(distance)))
# print("중간 거리인 정도 : " + str(middle(distance)))
# print("먼 거리인 정도 : " + str(high(distance)))