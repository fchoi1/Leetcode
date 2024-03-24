class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        heap = []
        countSet = defaultdict(int)
        counts = defaultdict(int)
        res = []
        for id, f in zip(nums, freq):
            if counts[id] in countSet:
                countSet[counts[id]] -= 1
                if countSet[counts[id]] == 0:
                    del countSet[counts[id]]
            counts[id] += f
            countSet[counts[id]] += 1
            
            heapq.heappush(heap, -counts[id])
            while heap and -heap[0] not in countSet:
                heapq.heappop(heap)
            res.append(-heap[0])
        return res