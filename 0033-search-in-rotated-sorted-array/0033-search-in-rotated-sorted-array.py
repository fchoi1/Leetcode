class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2
           

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                if target > nums[l]: #right side
                    l = mid + 1
                else:
                    r = mid 
            else:
                if target < nums[l]:
                    l = mid + 1
                else:
                    r = mid         
        return -1