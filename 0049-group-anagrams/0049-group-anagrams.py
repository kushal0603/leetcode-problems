class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for w in strs:
            anagrams[''.join(sorted(w))].append(w)
        return anagrams.values()