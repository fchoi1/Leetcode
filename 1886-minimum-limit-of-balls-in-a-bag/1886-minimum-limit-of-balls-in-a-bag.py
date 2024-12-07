class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        r = max(nums)
        l = 1

        while l < r:
            mid = (l + r) // 2
            split = 0
            for n in nums:
                if n <= mid:
                    continue
                split += n // mid
                split -= 1 if n % mid == 0 else 0
            if split <= maxOperations:
                r = mid 
            else:
                l = mid + 1
        return l


        