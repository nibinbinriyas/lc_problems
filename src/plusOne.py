def plusOne(digits):
  a=''.join(str(i) for i in digits)
  b = int(a)+1
  return [int(i) for i in str(b)]