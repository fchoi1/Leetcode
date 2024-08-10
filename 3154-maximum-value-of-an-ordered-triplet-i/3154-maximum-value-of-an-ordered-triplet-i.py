class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # preprocess
        val = 0
        N = len(nums)
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    val = max(val,(nums[i] - nums[j]) * nums[k])
                   
        return val


            