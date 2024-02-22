class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        total = int((1 + len(nums)) / 2 * len(nums))
        dupe = None
        for n in nums:
            if n in seen:
                dupe = n
            seen.add(n)
            total -= n
        return [dupe, dupe + total]
        
        