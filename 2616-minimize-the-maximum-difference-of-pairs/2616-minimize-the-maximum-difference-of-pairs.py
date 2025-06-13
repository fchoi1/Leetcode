class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # sort?
        nums.sort()
        #binary search

        def validPair(diff):
            count = 0
            i = 0
            while i + 1 < len(nums):
                if nums[i + 1] - nums[i] <= diff:
                    i += 2
                    count += 1
                else:
                    i += 1

            return count >= p

        l = 0
        r = max(nums)

        while l < r:
            mid = (l + r) // 2

            if validPair(mid):
                r = mid
            else:
                l = mid + 1
        return l