class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        # prime it always odd
        # 
        cache = {}

        for x in range(max(nums)):
            val = x | x + 1
            if val not in cache:
                cache[x | x + 1] = x
        for n in nums:
            if n not in cache:
                ans.append(-1)
            else:
                ans.append(cache[n])
        return ans
