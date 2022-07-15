class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    counts = Counter({0: 1})
    res = 0
    for total in accumulate(nums):
      res += counts[total - k]
      counts[total] += 1
    return res