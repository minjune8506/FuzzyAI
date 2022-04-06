from function_getDegreesOfMembership import getDegreesOfMembership
# 답장이 오는데 걸리는 시간 (분)

def low(answer):
    return getDegreesOfMembership(-1 , -1 , 10 , 40 , answer)

def medium(answer) :
    return getDegreesOfMembership(10 , 40 , 60 , 90 , answer)

def high(answer) :
    return getDegreesOfMembership(30 , 120 , -1 , -1 , answer)

answer = int(input("답장이 오는데 걸리는 시간(분) : "))
print("%.2f" %low(answer))
print("%.2f" %medium(answer))
print("%.2f" %high(answer))
