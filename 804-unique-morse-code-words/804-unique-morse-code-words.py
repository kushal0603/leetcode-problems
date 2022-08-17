class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        if len(words) == 1:
            return 1
        
        d = dict()
        ct = len(words)
        for i in words:
            s = ""
            for j in i:
                s+=morse[ord(j)-ord('a')]
            if s in d:
                ct-=1
            else:
                d[s] = 1
        
        return ct