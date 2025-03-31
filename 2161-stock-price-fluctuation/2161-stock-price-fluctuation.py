class StockPrice:

    def __init__(self):

        self.max = [] # max heap (price, timestamp)
        self.min = [] # min heap

        self.price = {}
        self.curr = -inf
        
    def update(self, timestamp: int, price: int) -> None:

        if self.max and self.max[0][1] == timestamp:
            heappop(self.max)

        if self.min and self.min[0][1] == timestamp:
            heappop(self.min)
        
        self.curr = max(self.curr, timestamp)

        self.price[timestamp] = price
        heappush(self.max, (-price, timestamp))
        heappush(self.min, (price, timestamp))
        
    def current(self) -> int:
        return self.price[self.curr]
        
    def maximum(self) -> int:
        while self.max and self.max[0][0] != -self.price[self.max[0][1]]:
            heappop(self.max)
        
        return -self.max[0][0]
        
    def minimum(self) -> int:
        while self.min and self.min[0][0] != self.price[self.min[0][1]]:
            heappop(self.min)
        
        return self.min[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()