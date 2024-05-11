class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        worker = []
        for q, w in zip(quality, wage):
            worker.append((w/q,q))
        ratio = sorted(worker, key= lambda x: x[0])
        heap = []
        maxR = -inf
        qTotal = 0
        for r,q in ratio[:k]:
            heapq.heappush(heap, -q)
            qTotal += q
        minWage = r * qTotal

        for r,q in ratio[k:]:
            if q < -heap[0]:
                qTotal += q + heapq.heappop(heap)
                heapq.heappush(heap, -q)
                minWage = min(minWage, r * qTotal)

        return minWage
