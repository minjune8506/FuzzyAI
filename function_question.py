#!/usr/bin/env python
# -*- coding: utf-8 -*-
#상대방이 보내는 물음표 갯수(일주일 기준)
from function_getDegreesOfMembership import getDegreesOfMembership

def low(question):
    return getDegreesOfMembership(-1,-1,10,20,question)

def middle(question):
    return getDegreesOfMembership(10,20,50,60,question)

def high(question):
    return getDegreesOfMembership(50,60,-1,-1,question)
