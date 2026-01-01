class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set()
        total = 0
        c = 0

        for n in nums:
            numSet.add(n)

        for n in numSet:
            if n-1 in numSet:
                continue
            else:
                while n in numSet:
                    n += 1
                    c += 1
                total = max(total, c)
                c = 0
        return total

            
        