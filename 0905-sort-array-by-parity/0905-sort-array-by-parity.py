class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        slow = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[slow] = nums[slow], nums[i]
                slow += 1
        return nums
