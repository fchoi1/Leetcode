class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        l = 1
        r = sum(quantities)
        mid = (l + r) // 2
        while l < r:
            mid = (l + r) // 2

            stores = sum(math.ceil(q/mid) for q in quantities)
            # print(l,r,mid,stores,n)
            if n == stores:
                r = mid
            elif n > stores:
                r = mid 
            else:
                l = mid + 1
        #     print("new", l, r)
        # print(l,r,mid)
        return l

        