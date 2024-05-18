# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # go left and right
        # check how many coins 
        moves = 0

        # count the level, that node is also how many coins we need
        def traverse(node):
            nonlocal moves
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            moves += abs(left) + abs(right)
            # print(left, right, node.val)
            return node.val + left + right - 1
        coins = traverse(root)
        print(coins)
        return moves
