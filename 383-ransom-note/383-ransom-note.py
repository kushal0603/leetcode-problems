class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = collections.Counter(magazine) # Count frequency of characters in magazine.
        
        for char in ransomNote:
			# If ransomNote has a character which is not present in count 
			# OR if the count of that character has become 0 , [eg: ransomNote = "aaa" and magazine = "aa"]
			# then return False
            if char not in count or count[char] == 0:
                return False
            # Decrease counter frequency by 1 at the end of each loop.
            count[char] -= 1
            
        return True
