class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s+=str(i)
        s = str(int(s)+1)
        l = list(s)
        for i in range(len(l)):
            l[i] = int(l[i])

        return l