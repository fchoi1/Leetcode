class AllOne:

    def __init__(self):
        self.countMap = defaultdict(set)
        self.dict = {}
        self.currMax = 0
        self.currMin = inf
    def inc(self, key: str) -> None:
        if key not in self.dict:
            self.dict[key] = 0

        self.dict[key] += 1
        
        self.currMax = max(self.currMax, self.dict[key])
        self.currMin = min(self.currMin, self.dict[key])

        if key in self.countMap[self.currMin] and len(self.countMap[self.currMin]) == 1:
            self.currMin += 1

        self.countMap[self.dict[key]-1].discard(key)
        self.countMap[self.dict[key]].add(key)

    def dec(self, key: str) -> None:
        if key not in self.dict:
            return

        self.dict[key] -= 1

        if self.dict[key] == 0:
            del self.dict[key]
            self.countMap[1].discard(key)
            if len(self.countMap[1]) == 0:
                self.currMin = inf
                for k,s in self.countMap.items():
                    if len(s) > 0:
                        self.currMin = min(self.currMin, k)
                        self.currMax = max(self.currMax, k)
            return
        if key in self.countMap[self.currMax] and len(self.countMap[self.currMax]) == 1:
            self.currMax -= 1

        self.currMax = max(self.currMax, self.dict[key])
        self.currMin = min(self.currMin, self.dict[key])

        self.countMap[self.dict[key]+1].discard(key)
        self.countMap[self.dict[key]].add(key)

    def getMaxKey(self) -> str:
        if len(self.countMap[self.currMax]) == 0:
            return ""
        return next(iter(self.countMap[self.currMax]))
        

    def getMinKey(self) -> str:
        if len(self.countMap[self.currMin]) == 0:
            return ""
        return next(iter(self.countMap[self.currMin]))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()