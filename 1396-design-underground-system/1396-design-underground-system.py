# 10 stations

class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.times = {} # start,end string, : entries, avg

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.times:
            print("err in check in", id)
        self.customer[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.customer:
            print("err in check out", id)
        else:
            startTime, startStation = self.customer[id]
            del self.customer[id]
            key = f'{startStation},{stationName}'
            diff = t - startTime
            if key in self.times:
                entries, avg = self.times[key]
                self.times[key] = (entries + 1, (avg * entries + diff)/(entries + 1))
            else:
                self.times[key] = (1, diff)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = f'{startStation},{endStation}'
        if key not in self.times:
            print("err in avg")
        return self.times[key][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)