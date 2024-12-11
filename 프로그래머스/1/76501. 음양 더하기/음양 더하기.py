def solution(absolutes, signs):
    answer = 0
    for abs_val, sign in zip(absolutes, signs):
        if sign:  # True이면 양수 그대로
            answer += abs_val
        else:  # False이면 음수
            answer -= abs_val
    return answer