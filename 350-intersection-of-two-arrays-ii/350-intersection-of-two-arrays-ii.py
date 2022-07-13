class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return functools.reduce(lambda prev, x: prev + [x[0]]*x[1], (collections.Counter(nums1)&collections.Counter(nums2)).items(), [])