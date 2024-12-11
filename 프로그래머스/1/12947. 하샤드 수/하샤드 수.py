def solution(x):
   #  a = sum((map(int, str(x))))
   if x % sum(map(int,str(x))) == 0:
      return True
   else: return False