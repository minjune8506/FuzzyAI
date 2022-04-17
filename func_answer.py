#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 답장이 오는데 걸리는 시간 (분)
from func_getDegreesOfMembership import getDegreesOfMembership

def low(answer):
    return getDegreesOfMembership(-1 , -1 , 10 , 40 , answer)

def middle(answer) :
    return getDegreesOfMembership(10 , 40 , 60 , 90 , answer)

def high(answer) :
    return getDegreesOfMembership(30 , 120 , -1 , -1 , answer)
