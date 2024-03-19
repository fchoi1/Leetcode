class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # start with highest freq
        count = Counter(tasks)
        heap = [-freq for val, freq in count.items()]
        print(heap)
        cycles = 0
        while heap:
            temp = []
            for i in range(n+1):
                if heap:
                    freq = heapq.heappop(heap)
                    freq += 1
                    if freq == 0:
                        if not heap and not temp:
                            cycles += i + 1
                            return cycles
                        continue
                    temp.append(freq)
            cycles += n+1
            for f in temp:
                heapq.heappush(heap, f)
            
        return cycles

        # wait full cycle, then pop back things into heap?

        