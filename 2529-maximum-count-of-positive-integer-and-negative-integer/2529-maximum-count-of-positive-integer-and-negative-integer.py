class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        # find zeros or switch

        # find above 0
        # find below 0
        N = len(nums)
        l = 0
        r = N - 1

        # find < 0
        while l < r:
            mid = (l + r + 1) // 2

            if nums[mid] >= 0:
                r = mid - 1
            else:
                l = mid
        
        neg = r

        if nums[r] == 0:
            neg = -1

        l = 0
        r = N - 1
        while l < r:
            mid = (l + r) // 2

            if nums[mid] <= 0:
                l = mid + 1
            else:
                r = mid
        pos = r

        if nums[r] == 0:
            pos += 1

        print(N, pos,  neg)

        return max(N - pos, neg + 1)
        
        