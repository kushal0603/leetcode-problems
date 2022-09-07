
class Solution:
    
    def recursion(self,root):
        if root == None:
            return ""
        
        left_string = self.recursion(root.left)
        right_string = self.recursion(root.right)
        if len(left_string)==0 and len(right_string)==0:
            return str(root.val)
        if len(left_string) != 0 and len(right_string) == 0:
            return str(root.val) +  "(" + left_string + ")"
        if len(left_string)==0 and len(right_string) != 0:
            return str(root.val) + "(" + ")" + "(" +right_string +")"
        return str(root.val) + "(" + left_string + ")" + "(" +right_string +")"
    
    
    def tree2str(self, root: Optional[TreeNode]) -> str:
        string =  self.recursion(root)
       
        
        return string