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
    print("distance : %d분, answer : %d분, count : %d번" %(distance, answer, count))
    print("거리 소속도 : %.1f" %function_distance.low(distance))
    print("답장 소속도 : %.1f" %function_answer.low(answer))
    print("만남 소속도 : %.1f" %function_count.low(count))
    premise = min(function_distance.low(distance), function_answer.low(answer), function_count.low(count))
    print("premise : %.1f" %premise)
    return function_socialize.middle(premise)

# Rule Number 2
# 거리 high and 만남 low and 물음표 low then 확률 very low
def rule_2(distance , count , question):
    print("rule_2")
    print("distance : %d분, count : %d번, question : %d번" %(distance, answer, question))
    print("거리 소속도 : %.1f" %function_distance.high(distance))
    print("만남 소속도 : %.1f" %function_count.low(count))
    print("물음표 소속도 : %.1f" %function_question.low(question))
    premise = min(function_distance.high(distance), function_count.low(count), function_question.low(question))
    print("premise : %.1f" %premise)
    return function_socialize.very_low(premise)

# Rule Number 3
# 거리 high and 만남 high and 답장 low then 확률 very high
def rule_3(distance , count , answer):
    print("rule_3")
    print("distance : %d분, answer : %d분, count : %d번" %(distance, answer, count))
    print("거리 소속도 : %.1f" %function_distance.low(distance))
    print("만남 소속도 : %.1f" %function_count.high(count))
    print("답장 소속도 : %.1f" %function_answer.low(answer))
    premise = min(function_distance.low(distance), function_count.high(count), function_answer.low(answer))
    print("premise : %.1f" %premise)
    return function_socialize.very_high(premise)

# Rule Number 4
# 거리 high and 만남 high and 답장 low and 물음표 high then 확률 very high
def rule_4(distance , count , answer , question):
    print("rule_4")
    print("distance : %d분, answer : %d분, count : %d번, question : %d번" %(distance, answer, count, question))
    print("거리 소속도 : %.1f" %function_distance.high(distance))
    print("만남 소속도 : %.1f" %function_count.high(count))
    print("답장 소속도 : %.1f" %function_answer.low(answer))
    print("물음표 소속도 : %.1f" %function_question.high(question))
    premise = min(function_distance.high(distance), function_count.high(count), function_answer.low(answer), function_question.high(question))
    print("premise : %.1f" %premise)
    return function_socialize.very_high(premise)

# Rule Number 5
# 거리 high and 만남 low then 확률 very low
def rule_5(distance , count):
    print("rule_5")
    print("distance : %d분, count : %d번" %(distance, count))
    print("거리 소속도 : %.1f" %function_distance.high(distance))
    print("만남 소속도 : %.1f" %function_count.low(count))
    premise = min(function_distance.high(distance) , function_count.low(count))
    print("premise : %.1f" %premise)
    return function_socialize.very_low(premise)

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

# Rule Number 11
# 답장 high or 물음표 low then 확률 low.
def rule_11(answer, question) :
    print("rule_11")
    print("answer : %d분, question : %d번" %(answer, question))
    print("답장 소속도 : %.1f" %(function_answer.high(answer)))
    print("물음표 소속도 : %.1f" %(function_question.low(question)))
    premise = max(function_answer.high(answer), function_question.low(question))
    print("premise : %.1f" %premise)
    return function_socialize.low(premise)

# Rule Number 12
# 답장 high and 물음표 high then 확률 high
def rule_12(answer, question) :
    print("rule_12")
    print("answer : %d분, question : %d번" %(answer, question))
    print("답장 소속도 : %.1f" %(function_answer.high(answer)))
    print("물음표 소속도 : %.1f" %(function_question.high(question)))
    premise = min(function_answer.high(answer), function_question.high(question))
    print("premise : %.1f" %premise)
    return function_socialize.high(premise)

# Rule Number 13
# 답장 low and 물음표 low then 확률 very low
def rule_13(answer, question) :
    print("rule_13")
    print("answer : %d분, question : %d번" %(answer, question))
    print("답장 소속도 : %.1f" %(function_answer.low(answer)))
    print("물음표 소속도 : %.1f" %(function_question.low(question)))
    premise = min(function_answer.low(answer), function_question.low(question))
    print("premise : %.1f" %premise)
    return function_socialize.very_low(premise)

# Rule Number 14
# 답장 high and 만남 high then 확률 high
def rule_14(answer, count) :
    print("rule_12")
    print("answer : %d분, count : %d번" %(answer, count))
    print("답장 소속도 : %.1f" %(function_answer.high(answer)))
    print("만남 소속도 : %.1f" %(function_count.high(count)))
    premise = min(function_answer.high(answer), function_count.high(count))
    print("premise : %.1f" %premise)
    return function_socialize.high(premise)

# Rule Number 15
# 답장 low and 만남 medium and 물음표 medium then 확률 medium
def rule_15(answer, count, question):
    print("rule_15")
    print("answer : %d분, count : %d번, question : %d번" %(answer, count, question))
    print("답장 소속도 : %.1f" %function_answer.low(answer))
    print("만남 소속도 : %.1f" %function_count.middle(count))
    print("물음표 소속도 : %.1f" %function_question.middle(question))
    premise = min(function_answer.low(answer), function_count.middle(count), function_question.middle(question))
    print("premise : %.1f" %premise)
    return function_socialize.middle(premise)

# Rule Number 16
# 답장 medium and 물음표 low then 확률 low
def rule_16(answer , question):
    print("rule_16")
    print("answer : %d분, question : %d번" %(answer, question))
    print("답장 소속도 : %.1f" %function_answer.middle(answer))
    print("물음표 소속도 : %.1f" %function_question.low(question))
    premise = min(function_answer.middle(answer) , function_question.low(question))
    print("premise : %.1f" %premise)
    return function_socialize.low(premise)

# Rule Number 17
# 물음표 low or 만남 low then 확률 medium
def rule_17(question, count):
    print("rule_17")
    print("question : %d번, count : %d번" %(question, count))
    print("물음표 소속도 : %.1f" %function_question.middle(question))
    print("만남 소속도 : %.1f" %function_count.low(count))
    premise = max(function_question.low(question), function_distance.low(count))
    print("premise : %.1f" %premise)
    return function_socialize.middle(premise)

# Rule Number 18
# 만남 high and 거리 high them 확률 high
def rule_18(count, distance) :
    print("rule_18")
    print("count : %d번, distance : %d분" %(count, distance))
    print("만남 소속도 : %.1f" %function_count.high(count))
    print("거리 소속도 : %.1f" %function_distance.high(distance))
    premise = min(function_count.high(count), function_distance.high(distance))
    print("premise : %.1f" %premise)
    return function_socialize.high(premise)

# Rule Number 19
# 만남 high or 물음표 high then 확률 medium
def rule_19(count, question) :
    print("rule_19")
    print("count : %d번, question : %d번" %(count, question))
    print("만남 소속도 : %.1f" %(function_count.high(count)))
    print("물음표 소속도 : %.1f" %(function_question.high(question)))
    premise = max(function_count.high(count), function_question.high(question))
    print("premise : %.1f" %premise)
    return function_socialize.middle(premise)

# Rule Number 20
# 만남 low then 확률 medium
def rule_20(count) :
    print("rule_20")
    print("count : %d번" %(count))
    print("만남 소속도 : %.1f" %(function_count.low(count)))
    premise = function_count.low(count)
    print("premise : %.1f" %premise)
    return function_socialize.middle(premise)

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
print(rule_11(answer, question))
print(rule_12(answer, question))
print(rule_13(answer, question))
print(rule_14(answer, count))
print(rule_15(answer, count, question))
print(rule_16(answer, question))
print(rule_17(question,count))
print(rule_18(count, distance))
print(rule_19(count, question))
print(rule_20(count))