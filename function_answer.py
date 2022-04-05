# 답장이 오는데 걸리는 시간 (분)

def low(answer):
    c = 10
    d = 40
    if (answer < c) :
        return 1
    elif (c <= answer < d) :
        return (d - answer) / (d - c)
    else :
        return 0

def medium(answer) :
    a = 10
    b = 40
    c = 60
    d = 90
    if (answer < a) :
        return 0
    elif (a <= answer < b) :
        return (answer - a) / (b - a)
    elif (b <= answer < c) :
        return 1
    elif (c <= answer < d) :
        return (d - answer) / (d - c)
    else :
        return 0

def high(answer) :
    a = 30
    b = 120
    if (answer < a) :
        return 0
    elif (a <= answer < b) :
        return (answer - a) / (b - a)
    else :
        return 1

answer = int(input("답장이 오는데 걸리는 시간(분) : "))
print("%.2f" %low(answer))
print("%.2f" %medium(answer))
print("%.2f" %high(answer))
