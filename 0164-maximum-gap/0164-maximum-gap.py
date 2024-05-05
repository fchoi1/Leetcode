class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        minVal , maxVal = min(nums), max(nums) 
        if maxVal - minVal == 0:
            return 0
        intervals = (maxVal - minVal) / (len(nums) - 1)
        buckets = [[inf, -inf] for _ in range(len(nums))]

        for n in nums:
            index = int((n-minVal) / intervals)
            if n < buckets[index][0]:
                buckets[index][0] = n
            if n > buckets[index][1]:
                buckets[index][1] = n

        maxDiff = 0
        prev = buckets[0][0]
        for a,b in buckets:
            if a == inf:
                continue
            if a-prev > maxDiff:
                maxDiff = a-prev
            prev = b
        return maxDiff 
        