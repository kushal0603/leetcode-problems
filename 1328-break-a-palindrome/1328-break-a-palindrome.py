class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ""
        for i, c in enumerate(palindrome):
            if c != 'a':
                break
        else:
            return palindrome[:-1]+'b'
        n = len(palindrome)
        if n%2 and i == n//2:
            return palindrome[:-1]+'b'
        return palindrome[:i]+'a'+palindrome[i+1:]