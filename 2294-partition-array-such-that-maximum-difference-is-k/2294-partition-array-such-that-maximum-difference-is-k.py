class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        q = deque([])

        curr = nums[0]
        count = 1
        for n in nums:
            if n - curr > k:
                curr = n
                count += 1
        return count 