class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        total = sum(candies)
        r = total // k
        print(total, r, k)
        l = 0

        def check(amount):
            piles = 0
            for c in candies:
                piles += c // amount
            return piles >= k
            

        mid = (l + r) // 2
        while l < r:
            mid = (l + r + 1) // 2 #  0 1 / 2 => 0 | 1 + 1 / 2 = 1

            if mid == 0:
                return r

            valid = check(mid)
            print(l,r,mid,"valid", valid)

            if check(mid):
                l = mid 
            else:
                r = mid - 1

        # print(target)
        print(l, r, mid)
        return l

        # bin search
        # can't combine
        