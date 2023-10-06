class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        fast = 0
        for slow, n in enumerate(nums):
            if fast < slow:
                fast = slow
            while nums[fast] == 0:
                fast += 1
                if fast == len(nums):
                    return
            if n == 0:
                nums[slow], nums[fast] = nums[fast],0

        