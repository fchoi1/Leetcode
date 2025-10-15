class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)

        def check(k):
            curr = deque([])
            increase = []

            for i in range(N):

                if curr and nums[i] > curr[-1]:
                    curr.append(nums[i])
                else:
                    curr = deque([nums[i]])
                
                if len(curr) > k:
                    curr.popleft()

                increase.append(len(curr) == k)
            for i in range(N-k):
                if increase[i] and increase[i + k]:
                    return True
            return False

        
        l = 0
        r = N // 2
        k = (l + r) // 2
        while l < r:
            k = (l + r + 1) // 2
            if k == 0:
                return 1
            if check(k):
                l = k 
            else:
                r = k - 1
        return l

        