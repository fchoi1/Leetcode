class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for n in nums:
            if nums[abs(n)-1] < 0:
                return abs(n)
            else:
                nums[abs(n)-1] = -nums[abs(n)-1]
        return -1 
        