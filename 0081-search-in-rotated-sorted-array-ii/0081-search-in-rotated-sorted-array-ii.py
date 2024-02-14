class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # if len(nums) == 1:
        #     return nums[0] == target
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right-left)//2
            if target in [nums[mid], nums[left], nums[right]]:
                return True
            
            if nums[left] == nums[right]:
                left += 1
                right -= 1
                continue

            
            if (target < nums[mid] and target > nums[left]) or (nums[left] > nums[mid] and (target < nums[mid] or target > nums[left])):
                right = mid 
            else:
                left = mid + 1

        return False
        