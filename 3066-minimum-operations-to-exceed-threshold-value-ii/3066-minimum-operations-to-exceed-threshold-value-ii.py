class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ops = 0
        while len(nums) > 1 and nums[0] < k:
            n1 = heappop(nums)
            n2 = heappop(nums)
            heappush(nums, n1 * 2 + n2)
            ops += 1
        return ops