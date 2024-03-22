class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        largest = nums[:k].index(max(nums[:k]))
        res = [nums[largest]]
        q = deque([largest])

        for i,n in enumerate(nums[k:]):
            if q and q[0] <= i:
                q.popleft()
        
            while q and nums[q[0]] <= n:
                q.popleft()
            q.append(i+k)
            res.append(nums[q[0]])

        return res