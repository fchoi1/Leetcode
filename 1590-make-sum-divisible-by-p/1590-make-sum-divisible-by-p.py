class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p 
        if remainder == 0:
            return 0
        keys = {0: -1}
        curr = 0
        minLen = inf
        for i,n in enumerate(nums):
            curr += n
            target = (curr % p - remainder) % p
            if target in keys:
                minLen = min(minLen, i - keys[target])
            keys[curr % p] = i

        return minLen if minLen < len(nums) else -1