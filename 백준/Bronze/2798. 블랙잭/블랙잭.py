from itertools import combinations
N, M = map(int,input().split())
numbers = list(map(int, input().split()))
maxsum = 0

for nthree in combinations(numbers,3):
    numsum = sum(nthree)

    if numsum <= M:
        if maxsum < numsum:
            maxsum = numsum
 
print(maxsum)
	