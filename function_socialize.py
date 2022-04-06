from function_getDegreesOfMembership import getDegreesOfMembership
def very_low(premise):
    return getDegreesOfMembership(-1 , -1 , 5 , 20 , premise)

def low(premise):
    return getDegreesOfMembership(5 , 20 , 30 , 45 , premise)

def middle(premise):
    return getDegreesOfMembership(30 , 45 , 55 , 70 , premise)

def high(premise):
    return getDegreesOfMembership(55 , 70 , 80 , 95 , premise)

def very_high(premise):
    return getDegreesOfMembership(80 , 95 , -1 , -1 , premise)

premise = float(input())

print("veryLow : " + str(very_low(premise)))
print("low : " + str(low(premise)))
print("middle : " + str(middle(premise)))
print("high : " + str(high(premise)))
print("veryhigh : " + str(very_high(premise)))