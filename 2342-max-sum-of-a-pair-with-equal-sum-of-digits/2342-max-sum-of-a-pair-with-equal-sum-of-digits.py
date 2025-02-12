class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        digit_map = {} # keep biggest
        largest = -1
        for n in nums:
            ds = sum(int(c) for c in str(n))
            if ds not in digit_map:
                digit_map[ds] = n
                continue
            largest = max(largest, digit_map[ds] + n)
            digit_map[ds] = max(digit_map[ds], n)

        return largest
        