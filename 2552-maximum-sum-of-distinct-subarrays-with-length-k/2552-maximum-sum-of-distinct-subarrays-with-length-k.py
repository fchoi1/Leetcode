class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        dupe = defaultdict(int)
        currSum = total = 0
        for i in range(k):
            dupe[nums[i]]+=1
            currSum += nums[i]
        if len(dupe) == k:
            total = currSum
        
        for i in range(len(nums)-k):
            currSum -= nums[i]
            currSum += nums[i+k]
            dupe[nums[i+k]]+=1
            dupe[nums[i]]-=1
            if dupe[nums[i]] <= 0:
                del dupe[nums[i]]
            if len(dupe) == k:
                total = max(total,currSum)
        
        return total



            

        