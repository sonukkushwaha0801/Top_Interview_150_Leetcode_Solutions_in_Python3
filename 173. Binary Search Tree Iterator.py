# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#Solution:
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.idx = 0
        self.values = self.getValues(root)
    
    def getValues(self, root: Optional[TreeNode]):
        values = []

        def dfs(node):
            if node:
                dfs(node.left)
                values.append(node.val)
                dfs(node.right)

        dfs(root)

        return values


    def next(self) -> int:
        node = self.values[self.idx]
        self.idx += 1

        return node

    def hasNext(self) -> bool:
        return self.idx < len(self.values)