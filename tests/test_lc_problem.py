from src.singleNumber import singleNumber
from src.lengthOfLastWord import lengthOfLastWord
from src.isPalindrome import isPalindrome
from src.plusOne import plusOne
from src.trailingZeroes import trailingZeroes

def test_singlNumber():
    assert singleNumber([2,2,1]) == 1

def test_lengthOfLastWord():
    assert lengthOfLastWord("   fly me   to   the moon  ") == 4

def test_isPalindrome():
    assert isPalindrome("A man, a plan, a canal: Panama") == True

def test_plusOne():
    assert plusOne([1,2,3]) == [1,2,4]
    
def test_trailingZeroes():
    assert trailingZeroes(5) == 1