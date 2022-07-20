class Solution:
    def numMatchingSubseq(self, S, words):
        res = 0
        for w,c in Counter(words).items():
            i, match = 0, True
            for x in w:
                i = S.find(x,i) + 1
                if not i:
                    match = False
                    break
            if match:
                res += c
        return res