class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sumDict = defaultdict(int)
        prefix = [0]            
        maxSum = float("-inf")
        for i,n in enumerate(nums):
            prefix.append(prefix[-1] + n)
            if n in sumDict:
                if prefix[i] <= prefix[sumDict[n]]:
                    sumDict[n] = i
            else:
                sumDict[n] = i
            if n-k in sumDict:
                maxSum = max(maxSum, prefix[i + 1] - prefix[sumDict[n-k]])
            if n+k in sumDict:
                maxSum = max(maxSum, prefix[i + 1] - prefix[sumDict[n+k]])
            
        return 0 if maxSum == float("-inf") else maxSum
                
 


        