class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxHeap = []
        minHeap = []
        removed = set()
        l = longest = 0

        for i,n in enumerate(nums):
            heapq.heappush(maxHeap, (-n, i))
            heapq.heappush(minHeap, (n, i))

            if -maxHeap[0][0] - minHeap[0][0] <= limit:
                longest = max(longest,i - l)
            else:
                while maxHeap and minHeap and -maxHeap[0][0] - minHeap[0][0] > limit:

                    if maxHeap[0][1] < minHeap[0][1]:
                        idx = heapq.heappop(maxHeap)[1]
                    else:
                        idx = heapq.heappop(minHeap)[1]
                    removed.add(idx)
                    l = max(l,idx+1) 

        return longest + 1