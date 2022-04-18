from rule_calculate import Fuzzy

def main() :
    distance = int(input("이성과의 집 거리(분) : "))
    answer = int(input("답장이 오는데 걸리는 시간(분) : "))
    count = int(input("한달동안 만나는 횟수(번) : "))
    question = int(input("일주일에 상대방이 보내는 물음표 갯수(개) : "))
    Fuzzy(distance, answer, count, question)

main()
