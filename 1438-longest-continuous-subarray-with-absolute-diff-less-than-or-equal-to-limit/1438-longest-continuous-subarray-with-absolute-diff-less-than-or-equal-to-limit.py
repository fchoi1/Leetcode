class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # sliding windows and heap?
        maxHeap = []
        minHeap = []
        removed = set()
        l = 0
        longest = 0

        for i,n in enumerate(nums):
            heapq.heappush(maxHeap, (-n, i))
            heapq.heappush(minHeap, (n, i))
            # print(i, "check", n)
            if -maxHeap[0][0] - minHeap[0][0] <= limit:
                longest = max(longest,i - l)
                # print(longest,"adding longest", i, l, maxHeap, minHeap)
            else:
                # print("pop heap")
                while maxHeap and minHeap and -maxHeap[0][0] - minHeap[0][0] > limit or (maxHeap[0][1] in removed or minHeap[0][1] in removed):

                    if maxHeap[0][1] in removed:
                        heapq.heappop(maxHeap)
                        continue
                    elif minHeap[0][1] in removed:
                        heapq.heappop(minHeap)
                        continue

                    if maxHeap[0][1] < minHeap[0][1]:
                        idx = heapq.heappop(maxHeap)[1]
                        removed.add(idx)
                        l = max(l,idx+1) 
                    else:
                        idx = heapq.heappop(minHeap)[1]
                        removed.add(idx)
                        l = max(l,idx+1) 
                

                # print("end",l, maxHeap, minHeap)
        return longest + 1

        # 8 8 8 8
        # 8 2 2 2

        # 7 7 7 8
        # 7 4 2 2
        