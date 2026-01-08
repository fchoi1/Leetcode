class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums) + 1
        missing = set(range(1,N))

        for n in nums:
            missing.discard(n)
        
        return list(missing)