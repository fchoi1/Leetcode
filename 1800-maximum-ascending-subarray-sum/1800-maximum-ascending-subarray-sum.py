class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        # dp

        largest = curr = nums[0]

        for a,b in zip(nums, nums[1:]):
            print(a,b, curr)
            if b > a:
                curr += b
            else:
                curr = b
            largest = max(curr, largest)
            
        return largest