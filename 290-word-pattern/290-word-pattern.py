class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return len(pattern)==len(s.split()) and len(set(pattern))==len(set(s.split()))==len(set(zip(pattern,s.split())))