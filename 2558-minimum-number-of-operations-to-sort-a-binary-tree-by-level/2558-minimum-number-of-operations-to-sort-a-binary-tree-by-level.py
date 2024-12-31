# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def getMinSwaps(arr):
            sorted_dict = {value: index for index, value in enumerate(sorted(arr))}
            visited = set()
            swaps = 0 
            for i,n in enumerate(arr):
                if n in visited:
                    continue
                visited.add(n)
                cycle = 0
                correct = sorted_dict[n]
                currN = n
                while correct != i:
                    cycle += 1
                    currN = arr[correct]
                    correct = sorted_dict[currN]
                    visited.add(currN) 
                swaps += max(0, cycle)
            return swaps

        ops = 0
        q = [root]

        while q:
            temp = []
            arr = []
            for n in q:
                arr.append(n.val)
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            ops += getMinSwaps(arr)
            q = temp
    
        return ops
        