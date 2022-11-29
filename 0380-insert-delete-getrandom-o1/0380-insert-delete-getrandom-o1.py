class RandomizedSet:

    def __init__(self):
        self.vals = {}  
        self.idxs = []

    def insert(self, val: int) -> bool:
        if val in self.vals : return False 
        self.vals[val] = len(self.idxs)
        self.idxs.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.vals: 
            lst = self.idxs[-1]     
            pos = self.vals[val]
            
            self.vals[lst] = pos               # move last value to the space
            self.idxs[pos] = lst               # occupied by the queried one...
            
            self.vals.pop(val)                 # ...and delete the respective
            self.idxs.pop()                    # data from both structures
            
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.idxs)