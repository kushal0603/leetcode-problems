class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # pattern for k > 1 is 
        if k > 1:
            # sort the string and return it as answer
            return ''.join(sorted(s))
        # for k = 1 case
        # check for each rotation, and update the min lexico string
        else:
            store = s
            for i in range(len(s)):
                s = s[k:] + s[:k]
                store = min(store,s)
            return store
    
    # one liner for above
    def orderlyQueue(self, s: str, k: int) -> str:
        return ''.join(sorted(s)) if k > 1 else min(s[pivot:] + s[:pivot] for pivot in range(len(s)))