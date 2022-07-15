from itertools import accumulate, islice
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [l*r for l, r in zip(chain([1], accumulate(nums, operator.mul)),islice(chain(reversed(list(accumulate(reversed(nums), operator.mul))), [1]), 1, None))]