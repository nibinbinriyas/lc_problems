def isPalindrome(s):
  a = ("".join(i for i in s if i.isalnum())).lower()
  pal = (lambda x:x == x[::-1])
  return pal(a)