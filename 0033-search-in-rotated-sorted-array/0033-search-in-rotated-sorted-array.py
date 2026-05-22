class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
        
            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[l]: # left side asc
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else: # right side asc
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid   
        return l if nums[l] == target else -1