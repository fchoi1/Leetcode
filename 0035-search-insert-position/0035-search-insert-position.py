class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right)//2
            print(mid, nums[mid])
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid 
        return left
        