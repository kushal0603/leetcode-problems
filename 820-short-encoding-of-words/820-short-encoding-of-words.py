class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        prev = self.root
        for i in word:
            if i not in prev:
                prev[i] = {}
            prev = prev[i]
            
    def count(self, root, level):
        if len(root) == 0: return level
        count = 0
        for i in root.keys():
            count += self.count(root[i], level + 1)
        return count
        
class Solution:
    def minimumLengthEncoding(self, words):
        words = map(lambda x:x[::-1],words)
        Obj = Trie()
        for word in words:
            Obj.insert(word)
        return Obj.count(Obj.root,1)