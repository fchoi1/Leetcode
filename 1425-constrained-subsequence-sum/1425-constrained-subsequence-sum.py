class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque([(nums[0], 0)])
        maxSum = nums[0]
        for i,n in enumerate(nums[1:]):
            currMax, index = q[0]
            localMax = max(n,currMax + n)
            maxSum = max(maxSum, localMax)
            if index <= i + 1 - k:
                q.popleft()
            while q and localMax > q[-1][0]:
                q.pop()
            q.append((localMax, i+1))

        return maxSum
                
 


        