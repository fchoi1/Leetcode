class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        minVal ,maxVal = min(nums), max(nums)
        r = (maxVal - minVal)
        if r == 0:
            return 0
        intervals = max(r / (len(nums) - 1),1)
        buckets = [(inf, -inf) for _ in range(len(nums))]

        print(intervals)
        for n in nums:
            index = int((n-minVal) / intervals)
            buckets[index] = (min(n,buckets[index][0]), max(n, buckets[index][1]))

        maxDiff = 0
        prev = buckets[0][0]
        for a,b in buckets:
            if a == inf:
                continue
            maxDiff = max(maxDiff, a-prev)
            prev = b
        return maxDiff 
        # 1 6 8 5 2
        

        # 1,2, 5, 6, 8

        # ans = 5,2