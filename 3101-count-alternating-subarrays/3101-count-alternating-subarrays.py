class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        prev = nums[0]
        slow = c = 0
        for i, n in enumerate(nums):
            if prev != n:
                c += i - slow + 1
            else:
                slow = i 
                c += 1
            prev = n
        return c 
        