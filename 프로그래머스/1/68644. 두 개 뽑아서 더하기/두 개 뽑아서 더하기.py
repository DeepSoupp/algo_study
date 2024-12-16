from itertools import combinations


def solution(numbers):
    answer = {sum(two) for two in combinations(numbers, 2)}
    return sorted(answer)