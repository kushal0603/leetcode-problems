class Solution:
    def reverseVowels(self, s: str) -> str:
        # To check if the character is Vowel or not
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # Left pointer
        l = 0
        # Right pointer
        r = len(s) - 1
        # convert s to List to be able to swap between vowels
        s_list = list(s)
        # Check till the two pointer meet.
        while l <= r :
            # if the two chars are vowels then swap
            if s_list[l] in vowels and s_list[r] in vowels:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
            # if the left char is the vowel only move the right pointer
            elif s_list[l] in vowels:
                r -= 1
            # if the right char is the vowel only move the left pointer
            elif s_list[r] in vowels:
                l += 1
            # if both are not vowels the move both pointers
            else:
                l += 1
                r -= 1
        return ''.join(s_list)