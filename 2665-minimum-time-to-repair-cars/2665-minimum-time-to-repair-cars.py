class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        # r * n ^ 2

        def canRepair(time):
            count = 0
            for r in ranks:
                count += floor(sqrt(time / r))
                if count > cars:
                    return True
            return count >= cars

        l = 0
        r = min(ranks) * cars * cars

        while l < r:
            mid  = (l + r) // 2

            if canRepair(mid):
                r = mid
            else:
                l = mid + 1

        
        print(l, r, mid)
        return l
        # b search?
        