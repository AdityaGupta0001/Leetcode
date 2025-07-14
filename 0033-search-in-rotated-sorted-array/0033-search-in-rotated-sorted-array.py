class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ctr = 0
        while ctr<len(nums):
            if nums[ctr] == target:
                break
            ctr+=1
        
        if ctr>=len(nums):
            return -1
        
        return ctr