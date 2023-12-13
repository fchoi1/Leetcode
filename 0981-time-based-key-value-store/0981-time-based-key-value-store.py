class TimeMap:

    def __init__(self):
        self.data = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        print(self.data)
        if key not in self.data:
            self.data[key] = [(value, timestamp)]
        else:
            self.data[key].append((value, timestamp))
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return  ""
        ts = self.data[key]
        left = 0
        right = len(ts) - 1
        #  1 4 6  -> timestamp = 3
        # left = 0, right = 2 half = 1

        while left < right:
            half = (left + right) // 2
            if timestamp < ts[half][1]:
                right = half
            if timestamp >= ts[half][1]:
                left = half + 1
        return ts[left][0]

        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)