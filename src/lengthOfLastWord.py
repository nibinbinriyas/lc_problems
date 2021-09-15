def lengthOfLastWord(s):
        l=0
        a=s.strip()
        print(len(a))
        print(a)
        for i in range(len(a)):
            if a[i]==" ":
                l=0
            else:
                l+=1
        return l