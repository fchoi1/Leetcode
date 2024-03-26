class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        N = len(nums)
        
        #  change negative and zero values
        for i in range(N):
            if nums[i] <= 0:
                nums[i] = N + 1

        for i in range(N):
            # Ignore numbers out of range
            if abs(nums[i]) <= N and nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1] 

        # final pass to check
        for i in range(N):
            if nums[i] > 0:
                return i + 1
        return N + 1
