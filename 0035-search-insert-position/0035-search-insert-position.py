class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        found = -1
        for i in range(len(nums)):
            if nums[i]==target:
                found = i

        if found==-1:
            l = nums
            l.append(target)
            l.sort()
            found = l.index(target)

        return found
