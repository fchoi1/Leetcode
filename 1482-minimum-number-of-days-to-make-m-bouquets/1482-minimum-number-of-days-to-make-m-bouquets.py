class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # sliding window of size k?
        # dp
        
        if len(bloomDay) < m * k:
            return -1
        
        r = max(bloomDay)
        l = 0

        # 0, 10
        # 5

        # 0 5
        # 2

        # 2 5
        # 3
        

        # 2 3
        # 2

        

        while l < r:
            mid = (l + r)//2

            consecutive = 0
            bouquets = 0

            for day in bloomDay:
                if day <= mid:
                    consecutive += 1
                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0

            if bouquets < m:
                l = mid + 1
            else:
                r = mid
        return l