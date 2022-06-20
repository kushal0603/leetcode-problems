class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n,m,k = n-1,m-1,n+m-1
        
        while m>=0 and n>=0:
            if nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                m-=1
            else:
                nums1[k] = nums2[n]
                n-=1
            k-=1
        while m>=0:
            nums1[k] = nums1[m]
            m,k = m-1,k-1
        while n>=0:
            nums1[k] = nums2[n]
            n,k = n-1,k-1
        