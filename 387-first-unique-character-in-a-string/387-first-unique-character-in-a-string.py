class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for idx, char in enumerate(s):
            if c[char] == 1:
                return idx
        return -1