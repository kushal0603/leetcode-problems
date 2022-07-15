class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        return min(len(s), 2 * sum(s.count(chr) // 2 for chr in set(s)) + 1)
        