#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Rules
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

# Rule Number 6
# 거리 medium and 만남 medium then 확률 medium
def rule_6(distance, count):
    print("rule_6")
    print("distance : %d분, count : %d번" %(distance, count))
    print("거리 소속도 : %.1f" %function_distance.middle(distance))
    print("물음표 소속도 : %.1f" %function_count.middle(count))
    premise = min(function_distance.middle(distance), function_distance.middle(count))
    print("premise : %.1f" %premise)
    return function_socialize.middle(premise)

# Rule Number 7
# 거리 high and 물음표 low then 확률 low
def rule_7(distance, question) :
    print("rule_7")
    print("distance : %d분, question : %d번" %(distance, question))
    print("거리 소속도 : %.1f" %function_distance.high(distance))
    print("물음표 소속도 : %.1f" %function_question.low(question))
    premise = min(function_distance.high(distance), function_question.low(question))
    print("premise : %.1f" %premise)
    return function_socialize.low(premise)

# Rule Number 8
# 답장 low and 만남 medium then 확률 medium
def rule_8(answer, count) :
    print("rule_8")
    print("answer : %d분, count : %d번" %(answer, count))
    print("답장 소속도 : %.1f" %(function_answer.low(answer)))
    print("만남 소속도 : %.1f" %(function_count.middle(count)))
    premise = min(function_answer.low(answer), function_count.middle(count))
    print("premise : %.1f" %premise)
    return function_socialize.middle(premise)

# Rule Number 9
# 답장 high and 물음표 high then 확률은 medium
def rule_9(answer, question) :
    print("rule_9")
    print("answer : %d분, question : %d번" %(answer, question))
    print("답장 소속도 : %.1f" %(function_answer.high(answer)))
    print("물음표 소속도 : %.1f" %(function_question.high(question)))
    premise = min(function_answer.high(answer), function_question.high(count))
    print("premise : %.1f" %premise)
    return function_socialize.middle(premise)

# Rule Number 10
# 답장 high and 물음표 low then 확률 low.
def rule_10(answer, question) :
    print("rule_10")
    print("answer : %d분, question : %d번" %(answer, question))
    print("답장 소속도 : %.1f" %(function_answer.high(answer)))
    print("물음표 소속도 : %.1f" %(function_question.low(question)))
    premise = min(function_answer.high(answer), function_question.low(count))
    print("premise : %.1f" %premise)
    return function_socialize.low(premise)

#안 사귈수가 없어야 함
distance = 15 # 거리 15분
answer = 10 # 답장 10분
count = 20 # 만남 20번
question = 100 # 물음표 100개

print(rule_1(distance , answer , count))
print(rule_2(distance , count , question))
print(rule_3(distance , count , answer))
print(rule_4(distance , count , answer , question))
print(rule_5(distance , count))
print(rule_6(distance, count))
print(rule_7(distance, question))
print(rule_8(answer, count))
print(rule_9(answer, question))
print(rule_10(answer, question))

