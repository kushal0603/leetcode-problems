class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        for i in range(0, len(l)):
            l[i] = "".join(reversed(l[i]))
        return " ".join(l)