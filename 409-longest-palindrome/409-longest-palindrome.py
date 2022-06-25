from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        longestPalin = 0
        counter = Counter(s)
        addedOne = False
        for c, freq in counter.items():
            if freq % 2:
                if not addedOne:
                    longestPalin += freq
                    addedOne = True
                else:
                    longestPalin += freq-1
            else:
                longestPalin += freq
        return longestPalin