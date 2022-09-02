class Solution:
    levelsList = []
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.levelsList = []
        currentLevel = 0
        output = []

        self.traverse(root, currentLevel)

        for level in self.levelsList:
            output.append(sum(level) / len(level))
            
        return output

    def traverse(self, root, currentLevel):
        if currentLevel < len(self.levelsList):
            self.levelsList[currentLevel].append(root.val)
        else:
            self.levelsList.append([root.val])
            
        if root.left:
            self.traverse(root.left, currentLevel + 1)
        if root.right:
            self.traverse(root.right, currentLevel + 1)