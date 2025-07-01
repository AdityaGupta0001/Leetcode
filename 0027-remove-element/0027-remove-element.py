class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        ctr=0
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]=-1
            else:
                ctr+=1

        nums.sort(reverse = True)

        return ctr