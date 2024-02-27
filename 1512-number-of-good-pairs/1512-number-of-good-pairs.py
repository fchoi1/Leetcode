class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        for i,n1 in enumerate(nums[:-1]):
            for n2 in nums[i+1:]:
                if n2 == n1:
                    c += 1
        return c

        