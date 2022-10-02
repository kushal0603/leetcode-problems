from collections import defaultdict

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        # [1] trivial cases
        if target > n*k : return 0
        if target < n   : return 0
        
        # [2] first roll of the dice
        n_of_ways = defaultdict(int)
        n_of_ways = {i:1 for i in range(1,k+1)}
        
        # [3] iterate over subsequent rolls 
        for i in range(2,n+1):
            n_of_ways_ = defaultdict(int)
            
            for j in range(1,k+1):
                for s, c in n_of_ways.items():
                    # [4] update 'number of ways' only if the current sum 
                    #     can be added up to 'target' in subsequent rolls
                    if s+j <= target - (n-i) and s+j >= target - (n-i)*k:
                        n_of_ways_[s+j] += c % 1000000007
            n_of_ways = n_of_ways_
        
        if target in n_of_ways:
            return n_of_ways[target] % 1000000007
        else:
            return 0 