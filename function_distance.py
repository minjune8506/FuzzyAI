def low(distance):
    c = 15
    d = 45
    
    if distance < c:
        return 1
    elif c <= distance < d:
        return (d - distance) / (d - c)
    else: # 굳이 안해줘도 되긴 하는데 의미 적으로 
        return 0

def middle(distance):
    a = 15
    b = 45
    c = 90
    d = 120
    
    if distance < a:
        return 0
    elif a <= distance < b:
        return (distance - a) / (b - a)
    elif b <= distance < c:
        return 1
    else:
        return (d - distance) / (d - c)

def high(distance):
    a = 90
    b = 120
    
    if distance < a:
        return 0
    elif a <= distance < b:
        return (distance - a) / (b - a)
    else:
        return 1

distance = int(input())

print("가까운 거리인 정도 : " + str(low(distance)))
print("중간 거리인 정도 : " + str(middle(distance)))
print("먼 거리인 정도 : " + str(high(distance)))