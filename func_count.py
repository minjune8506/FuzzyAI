#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 한달 동안 만나는 횟수 (번)
from func_getDegreesOfMembership import getDegreesOfMembership

def low(count):
    return getDegreesOfMembership(-1, -1, 0, 10, count)

def middle(count):
    return getDegreesOfMembership(5, 10, 15, 20, count)

def high(count):
    return getDegreesOfMembership(15, 25, -1, -1, count)
