class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        r,c = rStart, cStart
        order = []
        empty = False
        loop = 1
        print("rows", rows, cols)
        def addOrder(r,c):
            nonlocal empty
            print("add", r,c)
            if 0 <= r < rows and 0 <= c < cols:
                print("append", r,c)
                order.append((r,c))
                empty = False
        while not empty:
            empty = True
            # top
            for i in range(loop):
                addOrder(r,c)
                c += 1
            # right
            for i in range(loop):
                addOrder(r,c)
                r += 1
            # bottom
            for i in range(loop + 1):
                addOrder(r,c)
                c -= 1
            # left
            for i in range(loop + 1):
                addOrder(r,c)
                r -= 1
            loop += 2
        return order

        