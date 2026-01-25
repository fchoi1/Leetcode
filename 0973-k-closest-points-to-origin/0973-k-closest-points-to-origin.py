class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            dist = (x ** 2 + y ** 2) ** 0.5

            heappush(heap, (dist, (x,y)))

        return [heappop(heap)[1] for _ in range(k)]


        