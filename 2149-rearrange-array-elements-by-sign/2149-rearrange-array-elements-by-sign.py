class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        pos = 0
        neg = 0
        while pos < len(nums) and neg < len(nums):
            while pos < len(nums) and nums[pos] < 0:
                pos += 1
            while neg < len(nums) and nums[neg] > 0:
                neg += 1
            
            if pos < len(nums):
                res.append(nums[pos])
                pos += 1
            if neg < len(nums):
                res.append(nums[neg])
                neg += 1
        return res
        