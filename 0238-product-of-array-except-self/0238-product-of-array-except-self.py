class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]
        backward = [1]

        #   1  2 3   4
        # 1 1  2 6 24
        # 4 12 24 24
        # 24 24 12 4 1
        N = len(nums)
        for i in range(N):
            forward.append(nums[i] * forward[-1])
            backward.append(nums[N - i - 1] * backward[-1])
        
        res = []
        backward = backward[::-1]
        for i in range(1, N+1):
            res.append(forward[i-1] * backward[i])
        return res
        