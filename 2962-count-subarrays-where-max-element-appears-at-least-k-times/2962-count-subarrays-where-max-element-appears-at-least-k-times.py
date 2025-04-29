class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxEl = max(nums)
        total = n * (n+1) // 2
        counts = slow = neg = 0
        for i, n in enumerate(nums):
            if n == maxEl:
                counts += 1
            while counts >= k:
                if nums[slow] == maxEl:
                    counts -= 1
                slow += 1
            neg += i - slow + 1
        return total - neg



 