class MyCalendar:
    def __init__(self):
        self.eventDates = []

    def book(self, start: int, end: int) -> bool:
        for laststart,lastend in self.eventDates:
            if laststart < end and start < lastend: # means there is overlapping
                return False # so we can return False
        self.eventDates.append((start,end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)