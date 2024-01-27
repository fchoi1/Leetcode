class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        arraySum =  sum(nums)
        repeats = 0
        N = len(nums)
        if target > arraySum:
            repeats = target // arraySum
            target %= arraySum
        
        nums += nums
        currSum = left = 0
        smallest = None
        for i,n in  enumerate(nums):
            currSum += n
            while currSum > target:
                currSum -= nums[left]
                left+=1
            if currSum == target:
                smallest = i - left+1 if not smallest else min(smallest, i-left+1)
        return repeats * N + smallest if smallest != None else -1         