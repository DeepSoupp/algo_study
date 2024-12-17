def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        row = bin(arr1[i] | arr2[i])[2:].zfill(n)
        row = "".join(["#" if char == "1" else " " for char in row])

        answer.append(row)

    return answer