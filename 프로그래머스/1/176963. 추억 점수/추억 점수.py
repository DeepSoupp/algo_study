def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))

    for p in photo:
        point = 0
        for person in p:
            if person in dic:
                point += dic[person]
        answer.append(point)
    return answer