class TimeMap:

    def __init__(self):
        self.data = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
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
        while left < right:
            half = (left + right) // 2 +  1
            # if timestamp == ts[half][1]:
            #     return ts[half][0]
            if  timestamp < ts[half][1]:
                right = half - 1
            elif timestamp >= ts[half][1]:
                left =  half + 1
        return ts[right][0] if timestamp >= ts[right][1] else ""