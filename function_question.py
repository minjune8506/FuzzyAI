from function_getDegreesOfMembership import getDegreesOfMembership
#상대방이 보내는 물음표 갯수(일주일 기준)
def low(question):
    return getDegreesOfMembership(-1,-1,10,20,question)

def medium(question):
    return getDegreesOfMembership(10,20,50,60,question)

def high(question):
    return getDegreesOfMembership(50,60,-1,-1,question)

question = int(input("상대방이 보내는 물음표 갯수(일주일):"))

print("나에게 관심이 적다:"+str(low(question)))
print("나에게 관심이 적당히 있다:"+str(medium(question)))
print("나에게 관심이 많다:"+str(high(question)))