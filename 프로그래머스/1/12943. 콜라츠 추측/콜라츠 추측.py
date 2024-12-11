def solution(num):
   for answer in range(500):
      if num == 1:
         return answer
      num = num // 2 if num % 2 == 0 else num * 3 + 1
   return -1