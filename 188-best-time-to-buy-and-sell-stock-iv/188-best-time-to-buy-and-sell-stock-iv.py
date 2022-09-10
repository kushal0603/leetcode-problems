class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:            
        def dfs(index, prices, bought, k, dp):
            if index == len(prices) or k == 0:
                return 0

            if (index, k) in dp:
                return dp[(index, k)]
            
            op1 = op2 = op3 = 0
            
            # skip
            op1 = dfs(index + 1, prices,  bought, k, dp)
            
            if not bought:
                # buy
                op2 = -prices[index] + dfs(index + 1, prices, True, k - 1, dp)
            else:
                # sell
                op3 = prices[index] + dfs(index + 1, prices, False, k - 1, dp)
            
            dp[(index, k)] = max(op1, op2, op3)
            return dp[(index, k)]
         
        dp = {}
        return dfs(0, prices, False, 2 * k, dp)