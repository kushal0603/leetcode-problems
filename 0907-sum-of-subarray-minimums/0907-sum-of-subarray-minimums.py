class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        cache = 0
        stack = []
        count = []
        for val in arr:
            num = 1
            while stack and stack[-1] >= val:
                cache -= stack.pop() * count[-1]
                num += count.pop()
            stack.append(val)
            count.append(num)
            cache += val * num
            ans += cache
        return ans % (10**9 + 7)