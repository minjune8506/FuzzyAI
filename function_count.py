from function_getDegreesOfMembership import getDegreesOfMembership

def low(count):
    return getDegreesOfMembership(-1, -1, -1, 10, count)


def medium(count):
    return getDegreesOfMembership(5, 10, 15, 20, count)

    
def high(count):
    return getDegreesOfMembership(15, 25, -1, -1, count)

count = int(input("한달 동안 만나는 횟수(번)를 입력하시오 : "))

print("적다고 볼 수 있는 확률 : " + str(low(count)))
print("보통이라 볼 수 있는 확률 : " + str(medium(count)))
print("많다고 볼 수 있는 확률 : " + str(high(count)))
