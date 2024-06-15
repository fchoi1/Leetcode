class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxCap = 0
        cp = [(c, p, i) for i, (c,p) in enumerate(zip(capital, profits))]
        cp.sort()


        currCap = w
        projects = 0
        seen = set()
        heap = []
        for c,p,i in cp:
            if currCap >= c:
                heapq.heappush(heap, -p)
            else:
                if heap:
                    seen.add(i)
                    currCap -= heapq.heappop(heap)
                    projects += 1
                    if projects == k:
                        return currCap
                    if currCap >= c:
                        heapq.heappush(heap, -p)
                else:
                    break
        # print(c,p,i, currCap, heap)
            
        while projects < k and heap:
            currCap -= heapq.heappop(heap)
            projects += 1

        
        return currCap