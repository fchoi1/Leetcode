class Solution:
    def findMin(self, nums: List[int]) -> int:

        # binary search

        # start in middle
        # we need index of switching point

        #[4,5,6,7,0,1,2]  -> 4th index,  left  >  right
        #[4,5,6,0,1,2] ->  4th index    left  > right
        #[7,0,1,2,4,5,6] -> right  > left
        length = len(nums)
        left = 0
        right = length-1

        while left < right:
            mid = (left + right) // 2   
            if nums[left] < nums[right]: 
                return nums[left] 
            else:
                if nums[mid] >= nums[left]:
                    left = mid + 1
                else:
                    right = mid
        return nums[right]
