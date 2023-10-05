class RandomizedSet:

    def __init__(self):
        self.values = []
        self.map = collections.defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.values.append(val)
        self.map[val] = len(self.values) - 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        index = self.map[val]
        lastVal = self.values[-1]
        self.values[index], self.values[-1] = self.values[-1], self.values[index]
        self.map[lastVal] = index
        del self.map[val]
        self.values.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)