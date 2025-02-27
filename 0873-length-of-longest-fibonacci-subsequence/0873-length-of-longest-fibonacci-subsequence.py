class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        arrSet = set(arr)
        maxLen = 0
        seen = set()
        for i, a in enumerate(arr):
            for b in arr[i+1:]:
                currLen = 0
                prev = a
                curr = b
                if (a,b) in seen:
                    continue 
                while prev + curr in arrSet:
                    currLen += 1
                    prev,curr = curr, prev + curr
                    seen.add((prev,curr))
                if currLen:
                    maxLen = max(currLen + 2, maxLen)

        return maxLen

