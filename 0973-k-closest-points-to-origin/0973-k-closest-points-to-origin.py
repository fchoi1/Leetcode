import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dists = []
        for point in points:
            x,y = point
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(dists, (-dist, point))

            if len(dists) > k:
                heapq.heappop(dists)


        return  [dist[1] for dist in dists]     
        
        



        