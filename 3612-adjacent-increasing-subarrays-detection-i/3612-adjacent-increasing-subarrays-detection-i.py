class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

    
        curr = deque([])
        increase = []
        N = len(nums)

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





        
        