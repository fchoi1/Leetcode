# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        # store in   dict
        self.nodes = set()
        self.traverse(root, 0)

        # clean

    def traverse(self, node, val):
        if not node:
            return

        self.nodes.add(val)
        if node.left:
            node.left.val = val * 2 + 1
            self.traverse(node.left, node.left.val)
        
        if node.right:
            node.right.val = val * 2 + 2
            self.traverse(node.right, node.right.val)
        

        

    def find(self, target: int) -> bool:
        # retrieve from dict
        return target in self.nodes
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)