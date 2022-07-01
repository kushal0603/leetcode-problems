class Solution:
    def isValid(self, s):
        tracker = list()
        
        for c in s:
            if c == "(": tracker.append(")")
            elif c == "{": tracker.append("}")
            elif c == "[": tracker.append("]")
            else:
                if not tracker or tracker.pop() != c:
                    return False
            
        return not tracker