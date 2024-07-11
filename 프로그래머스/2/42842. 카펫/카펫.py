def solution(brown, yellow):
    total = brown + yellow
    #x는 3부터 total 나누기 3까지 돌면서 
    for x in range(3,int(total**0.5)+1):
        if total % x == 0:
            # x*y = total
            y = total // x
            #x-2 * y-2 = yellow의 값이 되는경우
            if (x-2)*(y-2) == yellow:
                return [y,x]
    return []
             
