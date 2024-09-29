class AllOne:

    def __init__(self):
        times = 50_000
        self.arr = [set() for _ in range(times)]
        self.dict = {}
        self.currMax = 0
        self.currMin = times - 1
        
    def inc(self, key: str) -> None:
        if key not in self.dict:
            self.dict[key] = 0

        self.dict[key] += 1
        
        self.currMax = max(self.currMax, self.dict[key])
        self.currMin = min(self.currMin, self.dict[key])

        if key in self.arr[self.currMin] and len(self.arr[self.currMin]) == 1:
            self.currMin += 1

        self.arr[self.dict[key]-1].discard(key)
        self.arr[self.dict[key]].add(key)

    def dec(self, key: str) -> None:
        if key not in self.dict:
            return

        self.dict[key] -= 1

        if self.dict[key] == 0:
            del self.dict[key]
            self.arr[1].discard(key)
            # print("dele",self.arr)
            if len(self.arr[1]) == 0:
                for i,s in enumerate(self.arr):
                    if len(s) > 0:
                        self.currMin = i
                        self.currMax = max(self.currMax, i)
                        break
            # print(self.currMax, self.currMin)
            return
        if key in self.arr[self.currMax] and len(self.arr[self.currMax]) == 1:
            self.currMax -= 1

        self.currMax = max(self.currMax, self.dict[key])
        self.currMin = min(self.currMin, self.dict[key])

        self.arr[self.dict[key]+1].discard(key)
        self.arr[self.dict[key]].add(key)

    def getMaxKey(self) -> str:
        # print(self.arr, self.currMax)
        if len(self.arr[self.currMax]) == 0:
            return ""
        return next(iter(self.arr[self.currMax]))
        

    def getMinKey(self) -> str:
        # print(self.arr, self.currMin)
        if len(self.arr[self.currMin]) == 0:
            return ""
        return next(iter(self.arr[self.currMin]))

        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()