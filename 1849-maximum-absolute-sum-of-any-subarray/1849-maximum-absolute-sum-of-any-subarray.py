class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # prefix?
        pre = [0]
        for n in nums:
            pre.append(pre[-1] + n)
        
        maxSum = -inf
        currMax = -inf
        currMin = inf
        print(pre)
        for p in pre[1:]:
            # print(currMax, currMin)
            currMax = max(p, currMax)
            currMin = min(p, currMin)
            maxSum = max(maxSum, currMax, abs(currMin), abs(p - currMax), abs(p - currMin))

        return maxSum
        