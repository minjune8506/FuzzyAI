#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Rules
import func_answer
import func_distance
import func_question
import func_count as func_count
import func_socialize
import numpy
import matplotlib.pyplot as plt

very_low = 0
low = 0
middle = 0
high = 0
very_high = 0

# Rule Number 0
# 물음표 low, 답장 high 확률 very_low
def rule_0(question, answer) :
    global very_low
    premise = max(func_question.low(question), func_answer.high(answer))
    very_low = max(very_low, premise)

# Rule Number 1
# 거리 high and 만남 low and 물음표 low 답장 high then 확률 very low
def rule_1(distance , count , question , answer):
    global very_low
    premise = min(func_distance.high(distance), func_count.low(count), func_question.low(question), func_answer.high(answer))
    very_low = max(very_low , premise)

# Rule Number 2
# 거리 high and 만남 low and 물음표 medium 답장 high then 확률 very low
def rule_2(distance , count , question , answer):
    global very_low
    premise = min(func_distance.high(distance), func_count.low(count), func_question.middle(question), func_answer.high(answer))
    very_low = max(very_low , premise)

# Rule Number 3
# 거리 high and 물음표 low then 확률 low
def rule_3(distance, question) :
    global low
    premise = min(func_distance.high(distance), func_question.low(question))
    low = max(low , premise)

# Rule Number 4
# 만남 low and 답장 high then 확률 low
def rule_4(count, answer):
    global low
    premise = min(func_count.low(count), func_answer.low(answer))
    low = max(low, premise)

# Rule Number 5
# 거리 medium and 답장 medium and 만남 medium then 확률 medium
def rule_5(distance , answer , count):
    global middle
    premise = min(func_distance.middle(distance), func_answer.middle(answer), func_count.middle(count))
    middle = max(middle , premise) 

# Rule Number 6
# 답장 low and 만남 low and 물음표 medium then 확률 medium
def rule_6(answer, count, question) :
    global middle
    premise = min(func_answer.low(answer), func_count.low(count), func_question.middle(question))
    middle = max(middle , premise)
    
# Rule Number 7
# 답장 low and 물음표 high and 거리 high then 확률 high
def rule_7(answer, question , distance) :
    global high
    premise = min(func_answer.low(answer), func_question.high(question) , func_distance.high(distance))
    high = max(high , premise)

# Rule Number 8
# 답장 low and 만남 medium then 거리 medium 확률 high
def rule_8(answer, count, distance) :
    global high
    premise = min(func_answer.low(answer), func_count.middle(count), func_distance.middle(distance))
    high = max(high , premise)

# Rule Number 9
# 거리 low and 만남 high and 답장 low and 물음표 medium then 확률 very high
def rule_9(distance , count , answer , question):
    global very_high
    premise = min(func_distance.low(distance), func_count.high(count), func_answer.low(answer) , func_question.high(question))
    very_high = max(very_high , premise)
    
# Rule Number 10
# 거리 low and 만남 high and 답장 low and 물음표 high then 확률 very high
def rule_10(distance , count , answer , question):
    global very_high
    premise = min(func_distance.low(distance), func_count.high(count), func_answer.low(answer), func_question.high(question))
    very_high = max(very_high , premise)

# Rule Number 11
# 만남 high or 답장 low then 사귈확률 very_high
def rule_11(count , answer):
    global very_high
    premise = max(func_count.high(count), func_answer.low(answer))
    very_high = max(very_high, premise)

def getPremise(distance, answer, count, question) :
    rule_1(distance , count , question , answer)
    rule_2(distance , count , question , answer)
    rule_3(distance, question)
    rule_4(count, answer)
    rule_5(distance , answer , count)
    rule_6(answer, count, question)
    rule_7(answer , question ,distance)
    rule_8(answer, count , distance)
    rule_9(distance , count , answer , question)
    rule_10(distance , count , answer , question)
    rule_11(count , answer)

def getCOG() :
	sum = 0
	p = 0 # 분모 
	for i in numpy.arange(0.0 , 100.01 , 0.1):
		# very_low 
		vl = very_low if func_socialize.very_low(i) >= very_low else func_socialize.very_low(i)
		# low
		l = low if func_socialize.low(i) > low else func_socialize.low(i)
		# middle
		m = middle if func_socialize.middle(i) > middle else func_socialize.middle(i)
		# high
		h = high if func_socialize.high(i) > high else func_socialize.high(i)
		# very_high
		vh = very_high if func_socialize.very_high(i) > very_high else func_socialize.very_high(i)
		sum += max(vl , l , m , h , vh) * i # 넓이의 합을 구한다
		p += max(vl , l ,  m , h , vh) # 분모에 구간들을 더해준다.
		# 그래프 그리기
	# 	plt.scatter(i , max(vl , l , m , h , vh) , c ='black' , edgecolor = 'black' , s = 1)
	# plt.show() # 그래프 표시
	print("사귈확률 : %.1f%%" %(sum / p)) # 무게중심 값

def Fuzzy(distance, answer, count, question) :
    getPremise(distance, answer, count, question)
    getCOG()
