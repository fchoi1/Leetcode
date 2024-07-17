# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        toDelete = set(to_delete)
        self.deleted = []
        def traverse(node, parent):
            if not node:
                return
            if not parent and node.val not in toDelete:
                self.deleted.append(node)
            if node.val in toDelete:
                if parent and parent.left == node:
                    parent.left = None
                elif parent:
                    parent.right = None

                traverse(node.left, None)
                traverse(node.right, None)

            else:
                traverse(node.left, node)
                traverse(node.right, node)
        traverse(root, None)
        return self.deleted
                
        