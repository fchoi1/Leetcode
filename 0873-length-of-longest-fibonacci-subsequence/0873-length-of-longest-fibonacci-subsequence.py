class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        arrSet = set(arr)
        maxLen = 0
        for i, a in enumerate(arr):
            for b in arr[i+1:]:
                currLen = 0
                prev = a
                curr = b 
                while prev + curr in arrSet:
                    currLen += 1
                    prev,curr = curr, prev + curr
                if currLen:
                    maxLen = max(currLen + 2, maxLen)

        return maxLen

