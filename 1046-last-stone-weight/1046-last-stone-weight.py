class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        
        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                stones.remove(stones[-2])
                stones.remove(stones[-1])
                
            else:
                stones[-1] = stones[-1] - stones[-2]
                stones.remove(stones[-2])
                stones = sorted(stones)
                
                
        return stones[0] if stones else 0