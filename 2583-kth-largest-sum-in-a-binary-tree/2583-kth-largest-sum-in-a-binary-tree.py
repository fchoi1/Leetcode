# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        q = [root]
        
        while q:
            currSum = 0
            temp = []
            for node in q:
                
                if node.right:
                    temp.append(node.right)

                if node.left:
                    temp.append(node.left)
                currSum += node.val
            
            heapq.heappush(heap, currSum)
            if len(heap) > k:
                heapq.heappop(heap)
            q = temp
        if len(heap) != k:
            return -1
        return heap[0]