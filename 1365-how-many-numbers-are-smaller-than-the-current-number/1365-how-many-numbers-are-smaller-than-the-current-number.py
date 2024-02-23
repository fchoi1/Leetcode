class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # sort
        count = [0] * (max(nums)+1)
        for n in nums:
            count[n] += 1
        for i in range(1,len(count)):
            count[i]+= count[i-1]
        count = [0] + count
        res = []
        for n in nums:
            res.append(count[n])
        return res
        