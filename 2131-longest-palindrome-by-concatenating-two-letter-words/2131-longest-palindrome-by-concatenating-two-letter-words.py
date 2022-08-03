from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq=Counter(words)
        resLength=0
        oddFlag=0
        for i in freq:
            rev=i[::-1]
            if rev in freq:
                if i!=rev:
                    possPair=min(freq[i],freq[rev])
                    resLength+=possPair*4
                    freq[rev]=0
                else:
                    resLength+=(freq[rev]//2)*4
                    if freq[i]%2!=0 and oddFlag==0:
                        oddFlag=1
                        resLength+=2
        return resLength