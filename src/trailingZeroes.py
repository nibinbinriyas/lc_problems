def trailingZeroes(n):
  fact = 1
  for i in range(1,n+1):
    fact = fact * i 
  s = str(fact)
  count = 0
  for i in range(len(s)-1,-1,-1):
    if s[i] == '0':
      count+=1
    else:
      break
  return count