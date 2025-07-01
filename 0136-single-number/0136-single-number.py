class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i]+=1

        num = 0
        for i in d.keys():
            if d[i] == 1:
                num = i
                break
            
        return num