class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        ones = nums.count(1)
        nums += nums
        curr = sum(x for x in nums[:ones])
        slow = 0
        swap = ones - curr
        for n in nums[ones:]:
            if nums[slow]:
                curr -= 1
            if n:
                curr += 1
            slow += 1
            swap = min(swap, ones-curr)
        return swap
            
            



