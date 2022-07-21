class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([k * n for k, n in sorted([(k, v) for k, v in Counter(s).items()], key=lambda t: t[1], reverse=True)])