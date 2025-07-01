import math
class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x==0:
            return 0
        elif x<0:
            neg = True
        x=abs(x)
        a1 = int(math.log10(x))
        a2 = 10**a1
        b = 1
        new_int = 0
        while a2!=0:
            new_int += (x//a2)*b
            x = x%a2
            a2 = a2//10
            b = b*10
        if new_int >= 2**31 -1:
            return 0
        if neg:
            new_int = -new_int
        return new_int