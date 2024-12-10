def solution(n):
    answer = 0
    # 약수를 구할때는 n 의 제곱근 까지 반복
    for i in range(1, int(n**(1/2))+1):
        if (n % i == 0):
            answer += i
            if i != n // i:
                answer += n // i
    return answer