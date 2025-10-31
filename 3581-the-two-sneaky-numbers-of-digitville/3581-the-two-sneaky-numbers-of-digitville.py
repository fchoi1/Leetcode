class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        i = 0
        ans = []
        while i < N:
            target = nums[i]
            if nums[i] != nums[target]:
                nums[i], nums[target] = nums[target], nums[i]
            else:
                i += 1
        return [nums[-1], nums[-2]]