class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        right = len(nums)
        seen = set()
        for left in range(right):
            right -= 1
            avg = (nums[left] + nums[right]) / 2
            seen.add(avg)
            if left >= right:
                return len(seen)
            
        return len(seen)