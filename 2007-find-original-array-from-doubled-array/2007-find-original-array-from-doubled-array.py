class Solution:
    from collections import Counter
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        changed.sort()
        length = len(changed)
        
        if length == 0 or length % 2 != 0:
            return []
        
        counter = Counter(changed)
        original = []
        
        for key in sorted(counter.keys()):
            
            if counter[key] == 0:
                continue
            elif key == 0:
                if counter[key] % 2 != 0:
                    return []
                else:
                    original.extend([key] * (counter[key] // 2))
            elif key * 2 not in counter or counter[key*2] < counter[key]:
                return []
            else:
                counter[key*2] -= counter[key]
                original.extend([key] * counter[key])
                
        
        return original