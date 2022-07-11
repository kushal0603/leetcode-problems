class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l = []
        i = 0 
        j = 0
        queue = [[root,j]]
        while queue:
            pop_element = queue.pop()
            if not pop_element[0] or (not pop_element[0].left and not pop_element[0].right):
                pass
            elif pop_element[0].left and pop_element[0].right:
                queue.insert(0,[pop_element[0].right,pop_element[1]+1])
                queue.insert(0,[pop_element[0].left,pop_element[1]+1])
            elif not pop_element[0].left:
                queue.insert(0,[pop_element[0].right,pop_element[1]+1])
            elif not pop_element[0].right:
                queue.insert(0,[pop_element[0].left,pop_element[1]+1])
            if(pop_element[1]==i):
                l.append(pop_element[0].val)
                i+=1
        
        return l