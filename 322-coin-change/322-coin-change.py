from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([0])
        for num in range(1, amount+1):
            if num in coins:
                queue.append(1)
            else:
                mini = float('inf')
                for coin in coins:
                    if num > coin:
                        index = num - coin
                        mini = min(mini, queue[index]+1)
                queue.append(mini)
        
        return queue[amount] if queue[amount] != float('inf') else -1