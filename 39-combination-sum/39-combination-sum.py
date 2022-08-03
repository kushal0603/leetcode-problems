class Solution:
    def combinationSum(self, c: List[int], t: int) -> List[List[int]]:
        ans = []
        
        def dfs(i,cur, tot):
            if tot == t:
                ans.append(cur.copy())
                return 
            if i>=len(c) or tot>t:
                return
            
            cur.append(c[i])
            dfs(i,cur,tot + c[i])
            cur.pop()
            
            dfs(i+1,cur,tot)
            
        dfs(0, [], 0)
        return ans