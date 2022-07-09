class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not str:
            return 0
        max_len = 0
        right = 0
        left = 0
        my_dict = {}
        while right < len(s):
            while s[right] in my_dict:
                my_dict.pop(s[left])
                left += 1
            my_dict[s[right]] = 1
            right += 1
            if len(my_dict) > max_len:
                max_len = len(my_dict)
        return max_len