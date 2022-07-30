class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        def count(a):
            rec = [0] * 26
            for char in a:
                rec[ord(char)-ord('a')] += 1
            return rec
        
        rec_B = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                rec_B[i] = max(rec_B[i], c)
        
        res = []
        for a in A:
            rec_a = count(a)
            if all(x >= y for x, y in zip(rec_a, rec_B)):
                res.append(a)
        return res