class Solution:
    def letterCasePermutation(self, s):
        return map(''.join, (set(product(*([i.lower(), i.upper()] for i in s)))))