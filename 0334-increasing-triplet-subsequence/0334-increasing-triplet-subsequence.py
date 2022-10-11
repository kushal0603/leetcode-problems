class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        smallest = second_smallest_right = float("inf")
        
        for i in nums:
            if i<smallest:
                smallest = i
            if i<second_smallest_right and i>smallest:
                second_smallest_right = i
            if i>second_smallest_right:
                return True
            
        return False