class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxCap = 0
        cp = [(c, p, i) for i, (c,p) in enumerate(zip(capital, profits))]
        cp.sort()

        currCap = w
        projects = 0
        heap = []
        for c,p,i in cp:
            if heap and c > currCap:
                currCap -= heapq.heappop(heap)
                projects += 1
                if projects == k:
                    return currCap
            elif not heap and c > currCap:
                break

            if currCap >= c:
                heapq.heappush(heap, -p)
            else:
                while heap and c > currCap:
                    currCap -= heapq.heappop(heap)
                    projects += 1
                    if projects == k:
                        return currCap
                if not heap and c > currCap:
                    return currCap
                heapq.heappush(heap, -p)
            
         
        # print(c,p,i, currCap, heap)
        print(len(heap))
        while projects < k and heap:
            currCap -= heapq.heappop(heap)
            projects += 1

        print(projects,k,currCap, len(heap))
        return currCap