class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # contains 0 
        # contains 0, 1
        

        # 4 1 0 2 3
        # [3,1,0,4,2]


        currMax = 0
        parts = 0
        for i,n in enumerate(arr):
            currMax = max(n, currMax)
            if currMax <= i:
                parts += 1
                currMax = 0
            
        return parts