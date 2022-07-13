class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_dist = 0
        
        for i in range(min(len(nums1), len(nums2))):
            
            if nums1[i] > nums2[i]:
                continue
            
            first_val = nums1[i]
            l, r = i, len(nums2) - 1
            while l <= r:
                j = (l+r)//2
                if first_val <= nums2[j]:
                    l = j + 1
                    
                else:
                    r = j - 1
                    
            max_dist = max(max_dist, r - i)
            
        return max_dist