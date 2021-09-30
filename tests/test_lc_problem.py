from src.singleNumber import singleNumber
from src.lengthOfLastWord import lengthOfLastWord
from src.isPalindrome import isPalindrome
from src.plusOne import plusOne
from src.trailingZeroes import trailingZeroes
from src.majorityElement import majorityElement
from src.isAnagram import isAnagram
from src.hammingWeight import hammingWeight
from src.isIsomorphic import isIsomorphic
from src.reverseString import reverseString
from src.isPowerOfFour import isPowerOfFour

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

def test_majorityElement():
    assert majorityElement([2,2,1,1,1,2,2]) == 2

def test_isAnagram():
    assert isAnagram("anagram","nagaram") == True

def test_hammingWeight():
    assert hammingWeight(11) == 3

def test_isIsomorphic():
    assert isIsomorphic("egg","add") == True

def test_reverseString():
    assert reverseString(["h","e","l","l","o"]) == ['o', 'l', 'l', 'e', 'h']

def test_isPowerOfFour():
    assert isPowerOfFour(16) == True