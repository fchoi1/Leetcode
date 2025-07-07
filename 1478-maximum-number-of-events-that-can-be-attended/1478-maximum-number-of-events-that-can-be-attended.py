class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        h = [] # end
        count = idx = curr = 0
 
        while idx < len(events) or h:
            while idx < len(events) and events[idx][0] <= curr:
                start, end = events[idx]
                heappush(h, end)
                idx += 1
            
            while h and h[0] < curr:
                heappop(h)
            
            if h:
                heappop(h)
                count += 1
            curr += 1
        return count
        