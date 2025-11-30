class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        target = sum(nums) % p
        if target == 0:
            return 0

        remain = {0:-1}
        smallest = inf
        curr = 0

        for i,n in enumerate(nums):
            curr += n
            r = curr % p
            key = (r - target) % p
            if key in remain:
                smallest = min(smallest, i - remain[key])
            remain[r] = i

        return smallest if smallest < len(nums) else -1