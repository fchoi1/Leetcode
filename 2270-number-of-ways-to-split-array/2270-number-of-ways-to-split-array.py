class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # prefix

        currSum = 0
        greater = 0
        prefx = [0]
        total = sum(nums)

        for n in nums[:-1]:
            currSum += n
            if currSum >= total - currSum:
                greater += 1
        return greater
