def solution(number, limit, power):
    attack_power = [0] * (number + 1 ) 

    for i in range(1, number + 1): 
        for j in range(i, number + 1, i):
            attack_power[j] += 1 

    total_weight = 0
    for i in range(1, number + 1):
        if attack_power[i] > limit: 
            total_weight += power
        else:
            total_weight += attack_power[i] 

    return total_weight