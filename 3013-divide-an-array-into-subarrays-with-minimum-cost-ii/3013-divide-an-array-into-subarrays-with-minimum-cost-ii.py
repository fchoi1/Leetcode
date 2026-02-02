class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # sliding window + heap

        maxHeap = []
        minHeap = []
        small = set()


        # construct heaps
        for i in range(1,dist + 2):
            heappush(maxHeap, (-nums[i], i))
            small.add(i)
            if len(maxHeap) > k - 1:
                val, idx = heappop(maxHeap)
                heappush(minHeap, (-val, idx))
                small.remove(idx)

        curr = sum(-h[0] for h in maxHeap)
        minCost = curr

        idx = dist + 2
        for n in nums[dist + 2:]:
            
            removeIdx = idx - dist - 1
            
            # remove stale idx
            while maxHeap and (maxHeap[0][1] <= removeIdx):
                heappop(maxHeap)

            while minHeap and (minHeap[0][1] <= removeIdx):
                heappop(minHeap)

            # push to minHeap first
            heappush(minHeap, (n, idx))

            # If we removed an index in small
            if removeIdx in small:
                curr -= nums[removeIdx]
                small.remove(removeIdx)

                sVal, sId = heappop(minHeap)
                heappush(maxHeap, (-sVal, sId))
                small.add(sId)
                curr += sVal
                
            # swap min and max heap vals
            if minHeap and maxHeap and minHeap[0][0] <= -maxHeap[0][0]:
                rVal, rId = heappop(maxHeap)
                sVal, sId = heappop(minHeap)

                small.remove(rId)
                curr += rVal

                small.add(sId)
                curr += sVal

                heappush(maxHeap, (-sVal, sId))
                heappush(minHeap, (-rVal, rId))

            minCost = min(minCost, curr)
            idx += 1
                
        return nums[0] + minCost