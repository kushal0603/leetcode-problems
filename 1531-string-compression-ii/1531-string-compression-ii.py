class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        def helper(s, cur, last, count, k, dp):
            # base case, no more chars to delete
            if k < 0:
                return float('inf')
            # base case, running the full length of s
            if cur >= len(s):
                return 0

            # if already memorized, reduce the complexity and directly return
            if (cur, last, count, k) in dp:
                return dp[(cur, last, count, k)]

            result = float('inf')
            # delete one char
            result = helper(s, cur + 1, last, count, k - 1, dp)
            # construct the string
            if s[cur] != last:
                # if not the same as the previous char
                result = min(result, 1 + helper(s, cur + 1, s[cur], 1, k, dp))
            else:
                # the same as the previous char
                # if the 2nd char (a->a2) and 10th char(a9->a10) and 100th char(a99->a100),
                # we need to add one more char.
                if count == 1 or count == 9 or count == 99:
                    result = min(result, 1 + helper(s, cur + 1, last, count + 1, k, dp))
                else:
                    # otherwise, concat the current char.
                    result = min(result, helper(s, cur + 1, last, count + 1, k, dp))

            # memorize
            dp[(cur, last, count, k)] = result
            return result

        return helper(s, 0, '#', 0, k, {})