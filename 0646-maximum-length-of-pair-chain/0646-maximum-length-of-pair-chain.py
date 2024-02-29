class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: (x[0], x[1]))
        heap = []
        count = 0
        curr = [-inf, -inf]
        for l, r in pairs:
            # while heap and l > heap[0][0]:
            #     right, left = heapq.heappop(heap)
            #     if curr[1] < left:
            #         count += 1  
            #         curr = [left, right]
            heapq.heappush(heap,[r,l])
        while heap:
            right, left = heapq.heappop(heap)
            if curr[1] < left:
                count += 1  
                curr = [left, right]
        return count