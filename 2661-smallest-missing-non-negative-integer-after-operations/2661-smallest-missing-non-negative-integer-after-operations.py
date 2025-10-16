class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:

        counts = [0 for _ in range(value)]
        for n in nums:
            counts[n % value] += 1

        minVal = min((c, i) for i, c in enumerate(counts))
        
        if minVal[1] == 0:
            if minVal[0] == 0:
                return 0
            return value * minVal[0]
        
        return minVal[1] + (minVal[0] * value)