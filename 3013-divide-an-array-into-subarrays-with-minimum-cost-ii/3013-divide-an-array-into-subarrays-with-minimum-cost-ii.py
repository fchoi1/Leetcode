class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # sliding window

        # heap
      
        
        # min cost heap length k
        maxHeap = []
        minHeap = []
        small = set()

        c = 0
        for i in range(1,dist + 2):
            heappush(maxHeap, (-nums[i], i))
            small.add(i)
            if len(maxHeap) > k - 1:
                val, idx = heappop(maxHeap)
                heappush(minHeap, (-val, idx))
                small.remove(idx)
            c += 1

        curr = sum(-h[0] for h in maxHeap)
        minCost = curr

        idx = dist + 2
        for n in nums[dist + 2:]:
            
            removeIdx = idx - dist - 1

            while maxHeap and (maxHeap[0][1] <= removeIdx):
                heappop(maxHeap)

            while minHeap and (minHeap[0][1] <= removeIdx):
                heappop(minHeap)

            # push to minHeap first
            heappush(minHeap, (n, idx))

            if removeIdx in small:
                curr -= nums[removeIdx]
                small.remove(removeIdx)

    
            # remove from maxHeap

            while (len(small) < k - 1 and minHeap):
                
             
                smallest, sId = heappop(minHeap)
                heappush(maxHeap, (-smallest, sId))

                small.add(sId)
                curr += smallest
            
            if minHeap and maxHeap:
                # swap min and max heap vals
                if minHeap[0][0] <= -maxHeap[0][0]:
                    rVal, rId = heappop(maxHeap)
                    small.remove(rId)
                    curr += rVal

                    smallest, sId = heappop(minHeap)
                    small.add(sId)
                    curr += smallest

                    heappush(maxHeap, (-smallest, sId))
                    heappush(minHeap, (-rVal, rId))

            minCost = min(minCost, curr)
            idx += 1
                

        return nums[0] + minCost