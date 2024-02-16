class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        forward = [1] * (N + 2)
        backward = [1] * (N + 2)
        result = []

        for i in range(N):
            forward[i+1] = nums[i] * forward[i]
            backward[N-i] = nums[-i-1] * backward[-i-1]
      
        for i in range(1,N+1):
            result.append(forward[i-1] * backward[i+1])
        return result