class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        for i in range(len(s)):
            subs = s[i:i+10]
            d[subs] = d.get(subs, 0) + 1
        return [c for c in d if d[c]>1]