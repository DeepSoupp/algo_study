def solution(numbers, target):
    def targetNumber(index, sum):
        if index == len(numbers):
            if sum==target:
                nonlocal answer
                answer+=1
            return
        targetNumber(index+1,sum+numbers[index])
        targetNumber(index+1,sum-numbers[index])
    answer = 0
    targetNumber(0,0)
    return answer