class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        total = 0
        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    total += 1
        return total