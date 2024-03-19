class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-freq for val, freq in count.items()]
        cycles = 0
        while heap:
            temp = []
            for i in range(n+1):
                if not heap:
                    break
                freq = heapq.heappop(heap)
                freq += 1
                if freq == 0 and not heap and not temp:
                    return cycles + i + 1
                elif freq != 0:
                    temp.append(freq)
            cycles += n+1
            for f in temp:
                heapq.heappush(heap, f)
            
        return -1


        