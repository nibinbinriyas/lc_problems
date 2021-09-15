from src.singleNumber import singleNumber
from src.lengthOfLastWord import lengthOfLastWord

def test_singlNumber():
    assert singleNumber([2,2,1]) == 1

def test_lengthOfLastWord():
    assert lengthOfLastWord("   fly me   to   the moon  ") == 4