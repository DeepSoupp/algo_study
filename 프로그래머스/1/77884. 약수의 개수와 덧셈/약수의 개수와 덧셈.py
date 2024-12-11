def solution(left, right):
    answer = 0
    divlist = []
    for num in range(left, right + 1):
        for i in range(1, int(num ** (1 / 2)) + 1):
            if num % i == 0:
                divlist.append(i)
                if (i**2) != num:
                    divlist.append(num // i)
        if len(divlist) % 2 == 0:
            answer += num
        else:
            answer -= num
        divlist = []
    return answer