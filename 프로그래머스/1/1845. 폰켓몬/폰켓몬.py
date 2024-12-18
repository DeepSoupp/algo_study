def solution(nums):

    uni = len(set(nums))
    pick = len(nums) // 2

    return min(uni, pick)