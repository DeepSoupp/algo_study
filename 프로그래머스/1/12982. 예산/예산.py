def solution(d, budget):
    answer = 0
    d = sorted(d)
    money = 0
    for i in d:
        if money + i <= budget:
            money += i
            answer += 1
        else:
            break
    return answer