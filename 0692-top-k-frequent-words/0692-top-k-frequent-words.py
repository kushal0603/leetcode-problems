class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=Counter(words)
        d=dict(sorted(d.items(),key=lambda items:(-items[1],items[0])))
        return list(d.keys())[:k]