#!/usr/bin/env python
# -*- coding: utf-8 -*-

import function_answer
import function_distance
import function_question
import function_count
import function_socialize

# Rule Number 1
# 거리 low and 답장 low and 만남 low then 확률 medium
def rule_1(distance , answer , count):
    print("rule_1")
    print(distance , answer , count)

    print(function_distance.low(distance))
    print(function_answer.low(answer))
    print(function_count.low(count))
    
    return function_socialize.middle_area(min(function_distance.low(distance) , 
    function_answer.low(answer) , function_count.low(count)))

# Rule Number 2
# 거리 high and 만남 low and 물음표 low then 확률 very low
def rule_2(distance , count , question):
    print("rule_2")
    print(distance , count , question)

    print(function_distance.high(distance))
    print(function_count.low(count))
    print(function_question.low(question))

    return function_socialize.very_low_area(min(function_distance.high(distance) , 
    function_count.low(count) , function_question.low(question)))

# Rule Number 3
# 거리 high and 만남 high and 답장 low then 확률 very high
def rule_3(distance , count , answer):
    print("rule_3")
    print(distance , count , answer)

    print(function_distance.high(distance))
    print(function_count.high(count))
    print(function_answer.low(answer))

    return function_socialize.very_high_area(min(function_distance.high(distance) , 
    function_count.high(count) , function_answer.low(answer)))

# Rule Number 4
# 거리 high and 만남 high and 답장 low and 물음표 high then 확률 very high
def rule_4(distance , count , answer , question):
    print("rule_4")
    print(distance , count , answer , question)

    print(function_distance.high(distance))
    print(function_count.high(count))
    print(function_answer.low(answer))
    print(function_question.high(question))

    return function_socialize.very_high_area(min(function_distance.high(distance) , 
    function_count.high(count) , function_answer.low(answer) , function_question.high(question)))

# Rule Number 5
# 거리 high and 만남 low then 확률 very low
def rule_5(distance , count):
    print("rule_5")
    print(distance , count)

    print(function_distance.high(distance))
    print(function_count.low(count))

    return function_socialize.very_low_area(min(function_distance.high(distance) , function_count.low(count)))


distance = 15 # 거리 15분
answer = 10 # 답장 10분
count = 20 # 만남 20번
question = 100 # 물음표 100개

#안 사귈수가 없어야 함
print(rule_1(distance , answer , count))
print(rule_2(distance , count , question))
print(rule_3(distance , count , answer))
print(rule_4(distance , count , answer , question))
print(rule_5(distance , count))