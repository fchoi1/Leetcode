class MyCalendarTwo:

    def __init__(self):
        self.booked = [] 

    def book(self, start: int, end: int) -> bool:
        # print(self.booked, (start, end))
        if not self.booked:
            self.booked.append((start, end))
            return True
        q = []
        
        temp = sorted(self.booked + [(start,end)])

        for s,e in temp:
            if q and s >= q[0]:
                heappop(q)
            heappush(q, e)

        if len(q) > 2:
            return False

        self.booked.append((start,end))
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)