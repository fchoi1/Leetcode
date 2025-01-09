class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left = 0
        right = length - 1
        mid = (left + right) // 2
        if nums[mid] == target: return mid
        while left < right:
            # 
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid 
                else:
                    left = mid + 1
            else: # spicy logic
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid 
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

        return -1