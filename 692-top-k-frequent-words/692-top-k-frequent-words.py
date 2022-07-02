class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = defaultdict(int)
        for s in words:  freq[s] -= 1     
        res = []
        
        for s, f in sorted(freq.items(), key=lambda x: (x[1], x[0])):
            k -= 1
            res.append(s)
            if not k: return res
            