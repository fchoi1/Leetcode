# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def comparePath(treeNode, listNode):
            if not listNode:
                return True
            if not treeNode or listNode.val != treeNode.val:
                return False
            return comparePath(treeNode.left, listNode.next) or comparePath(treeNode.right, listNode.next)
        
        def dfs(node):
            if not node:
                return False
            
            if node.val == head.val:
                if comparePath(node, head):
                    return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
            

        