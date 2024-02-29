class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        heap = []
        count = 0
        curr = [-inf, -inf]
        for l, r in pairs:
            heapq.heappush(heap,[r,l])
            
        while heap:
            right, left = heapq.heappop(heap)
            if curr[1] < left:
                count += 1  
                curr = [left, right]
        return count