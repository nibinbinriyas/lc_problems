from math import log
def isPowerOfFour(n):
    if n < 1:
            return False
    power = log(n) / log(4)
    return power == int(power)