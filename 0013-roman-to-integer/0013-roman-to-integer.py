class Solution:
    def romanToInt(self, s: str) -> int:
        translation = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        index = {'I':0,'V':1,'X':2,'L':3,'C':4,'D':5,'M':6}

        out = 0

        skip=[]
        ctr=0
        add = []
        subtract = []

        for i in range(len(s)-1):
            if i in skip:
                continue
            elif index[s[i]]>=index[s[i+1]]:
                add.append(s[i])
                ctr+=1
            else:
                subtract.append(s[i]+s[i+1])
                skip.append(i+1)
                ctr+=2
        if ctr!=len(s):
            add.append(s[-1])

        for a in add:
            out+=translation[a]
        
        for sub in subtract:
            out+=translation[sub[-1]]-translation[sub[0]]

        return out