class Solution:
	def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:

		length = len(multipliers)

		dp = [[0] * (length + 1) for _ in range(length + 1)]

		for multi in range(length - 1, -1, -1):

			for index in range(multi, -1, -1):

				left_output = multipliers[multi] * nums[index] + dp[multi + 1][index + 1]
				right_output = multipliers[multi] * nums[len(nums) - 1 - multi + index] + dp[multi + 1][index]
				dp[multi][index] = max(left_output, right_output)

		return dp[0][0] 