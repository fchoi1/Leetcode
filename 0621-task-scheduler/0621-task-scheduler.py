import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasklist = [0]* 26
        for task in tasks:
            index = ord(task) - ord('A')
            tasklist[index] += 1
        
        available = []
        for count in tasklist:
            if count != 0:
                heapq.heappush(available, -count)
        
        q = deque([])
        time = 0
        while len(available) > 0 or len(q) > 0:
            time += 1
            if len(available) > 0:
                count = heapq.heappop(available) + 1
                if count:
                    q.append((count,time + n ))
            while len(q) > 0 and q[0][1] == time:
                c,t = q.popleft()
                heapq.heappush(available, c)
            
        return time 
        