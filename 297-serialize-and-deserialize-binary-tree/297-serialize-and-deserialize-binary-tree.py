class Codec:

    def serialize(self, root):
        ans=[]
        def dfs(r):
            if not r:
                ans.append("N")
                return
            ans.append(str(r.val))
            dfs(r.left)
            dfs(r.right)
        dfs(root)
        return ','.join(ans)
        

    def deserialize(self, data):
        ans=data.split(",")
        self.p=0
        def dfs():
            if ans[self.p]=="N":
                self.p+=1
                return None
            node=TreeNode(int(ans[self.p]))
            self.p+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()