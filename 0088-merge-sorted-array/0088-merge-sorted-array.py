class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        replace = len(nums1)-len(nums2)
        ctr = 0
        for i in range(replace,len(nums1)):
            nums1[i] = nums2[ctr]
            ctr+=1
        
        nums1.sort()