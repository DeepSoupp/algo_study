def solution(k, score):
    answer = []
    rank = []
    for sc in score:
        if len(rank) < k:
            rank.append(sc)
            rank.sort()
        else:
            if sc > rank[0]:
                rank[0] = sc
                rank.sort()
        answer.append(rank[0])
    return answer