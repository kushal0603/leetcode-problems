class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0
        def dfs(i, bitmask, length):
            nonlocal ans
            ans = max(ans, length)
            if i == len(arr):
                return
            # cache for backtrack
            prev_bitmask = bitmask
            for ch in arr[i]:
                if 1 << (ord(ch)-ord('a')) & bitmask != 0:
                    # duplicates if we add arr[i]
                    dfs(i+1, prev_bitmask, length)
                    return
                bitmask |= 1<<(ord(ch)-ord('a'))
            # either add arr[i] to subsequence
            dfs(i+1, prev_bitmask, length)
            # or skip arr[i]
            dfs(i+1, bitmask, length+len(arr[i]))
            return
        dfs(0, 0, 0)
        return ans