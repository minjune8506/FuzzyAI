#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 상대방 집까지 걸리는 시간 (분)
from func_getDegreesOfMembership import getDegreesOfMembership

def low(distance):
    return getDegreesOfMembership(-1 , -1 , 15 , 45 , distance)

def middle(distance):
    return getDegreesOfMembership(15 , 45 , 90 , 120 , distance)
        
def high(distance):
    return getDegreesOfMembership(90 , 120 , -1 , -1 , distance)
