def isIsomorphic(s,t):
    if len(s) != len(t):
        return False
    return len(set(s)) == len(set(t)) == len(set(zip(s,t)))