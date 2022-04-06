def very_low(premise):
    c = 5
    d = 20

    if premise < c:
        return 1
    elif c <= premise < d:
        return (d - premise) / (d - c)
    else:
        return 0

def low(premise):
    return all_parameter_calculate(5 , 20 , 30 , 45 , premise)

def middle(premise):
    return all_parameter_calculate(30 , 45 , 55 , 70 , premise)

def high(premise):
    return all_parameter_calculate(55 , 70 , 80 , 95 , premise)

def very_high(premise):
    a = 80
    b = 95

    if premise < a:
        return 0
    elif a <= premise < b:
        return (premise - a) / (b - a)
    else:
        return 1

def all_parameter_calculate(a , b , c , d , premise):
    if premise < a:
        return 0
    elif a <= premise < b:
        return (premise - a) / (b - a)
    elif b <= premise < c:
        return 1
    elif c <= premise < d:
        return (d - premise) / (d - c)
    else:
        return 0

premise = float(input())

print("veryLow : " + str(very_low(premise)))
print("low : " + str(low(premise)))
print("middle : " + str(middle(premise)))
print("high : " + str(high(premise)))
print("veryhigh : " + str(very_high(premise)))