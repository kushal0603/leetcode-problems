class Solution:
    def longestPalindrome(self, s: 'str') -> 'str': # O(n^2) time, O(n) space [O(1) extra space]

        def expand(i, j, string = s):   # O(n) time, O(1) space
            while i >= 0 and j < len(string):
                if string[i] != string[j]: break
                i, j = i-1, j+1
            return i+1, j
        
        indices = 0, 0    # start and end indices of Longest Palindromic Substring
        for i, _ in enumerate(s): 
            indices = max([indices, expand(i, i), expand(i, i+1)], key = lambda j: j[1] - j[0]) # j...index
        return s[indices[0] : indices[1]]