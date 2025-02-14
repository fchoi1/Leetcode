class ProductOfNumbers:

    def __init__(self):

        self.products = [(1, 0)]
        

    def add(self, num: int) -> None:
        prev, zeros = self.products[-1]
        if not num:
            num = 1
            zeros += 1
        entry = (prev * num,zeros)
        self.products.append(entry)
        

    def getProduct(self, k: int) -> int:
        curr, currZeros = self.products[-1]
        prev, prevZeros = self.products[-k-1]
        if currZeros > prevZeros:
            return 0

        return int(curr / prev)
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# 3 , 2, 2
# 3 6 12
# 