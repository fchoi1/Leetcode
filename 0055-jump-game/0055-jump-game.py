class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = 0
        for n in nums[::-1]:
            target = 1 if n >= target else target + 1
        return target == 1
