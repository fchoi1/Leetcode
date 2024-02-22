class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        diff = int((1 + len(nums)) / 2 * len(nums)) - sum(nums)
        for n in nums:
            if n in seen:
                return [n, n + diff]
            seen.add(n)
        return []
        
        