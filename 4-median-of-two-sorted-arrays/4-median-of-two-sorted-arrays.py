class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
         nums1.append(i)
        
         nums1 = sorted(nums1)
    
        length_nums1 = len(nums1)
    
        if length_nums1 % 2 == 0:
         return (nums1[length_nums1//2] + nums1[length_nums1//2 - 1])/2
    
        else:
         return nums1[length_nums1//2]
