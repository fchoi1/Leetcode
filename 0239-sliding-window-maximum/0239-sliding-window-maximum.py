class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        heap = []
        for n in nums[:k]:
            count[n] += 1
            heapq.heappush(heap, -n)

        slow = 0
        maxArr = [-heap[0]]
        for n in nums[k:]:
            count[nums[slow]] -= 1
            count[n] += 1
            heapq.heappush(heap, -n)
            while count[-heap[0]] == 0:
                heapq.heappop(heap)
            maxArr.append(-heap[0])
            slow += 1
        return maxArr