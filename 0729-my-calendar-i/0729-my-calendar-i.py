class MyCalendar:

    def __init__(self):
        self.heap = []
        
    def book(self, start: int, end: int) -> bool:
        # print("book", self.heap, (start,end))
        if not self.heap or end <= self.heap[0][0]:
            heappush(self.heap, (start,end))
            return True

        temp = []
        currTime = nextTime = None
        noOverlap = False
    
        while self.heap and start >= self.heap[0][1]:
            currTime = heappop(self.heap)
            # print("popped", currTime)
            heappush(temp, currTime)

        # print("here", currTime,  (start, end), temp, self.heap)
        if not currTime:
            currTime = heappop(self.heap)
            heappush(temp, currTime)

        if self.heap:
            if start >= currTime[1] and end <= self.heap[0][0]:
                heappush(temp, (start,end))
                noOverlap = True
        else:
            if start >= currTime[1]:
                heappush(temp, (start,end))
                noOverlap = True

        while self.heap:
            heappush(temp, heappop(self.heap))
        self.heap = temp
        # print("end", self.heap)
        return noOverlap
