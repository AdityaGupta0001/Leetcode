class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # s = ""
        # s1 = set()
        # for i in nums:
        #     s+=str(abs(i))
        #     s1.add(i)
        # if len(s1) == len(s):
        #     return False
        # else:
        #     return True

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        
        return False