class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        count = 0
        currMax = -inf
        q = deque([])
        maxHeap = [] # val, index
        minHeap = [] # val, index

        for r, n in enumerate(nums):
            while maxHeap and abs(-maxHeap[0][0] - n) > 2:
                index = maxHeap[0][1]
                while q and q[0][1] <= index:
                    q.popleft()
                heappop(maxHeap)

            while minHeap and abs(minHeap[0][0] - n) > 2:
                index = minHeap[0][1]
                while q and q[0][1] <= index:
                    q.popleft()
                heappop(minHeap)
                # print("min", index, q)
             
            q.append((n,r))
            heappush(maxHeap, (-n,r))
            heappush(minHeap, (n,r))
            count += len(q)
            # print(q, len(q), maxHeap, minHeap)

        return count 
                
                

