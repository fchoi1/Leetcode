class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = [{"val": value, "times":[timestamp]}]
        else:
            self.data[key][-1]["times"].append(timestamp - 1)
            self.data[key].append({"val": value, "times":[timestamp]})
            
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        if timestamp >= self.data[key][-1]["times"][0]:
            return self.data[key][-1]["val"]
        
        minIndex = 0
        maxIndex = len(self.data[key])
        
        while maxIndex > minIndex:
            half = (maxIndex + minIndex) // 2
            if timestamp < self.data[key][half]["times"][0]:
                maxIndex = half
            elif timestamp > self.data[key][half]["times"][1]:
                minIndex = half
            else:
                return self.data[key][half]["val"]
        return ""

