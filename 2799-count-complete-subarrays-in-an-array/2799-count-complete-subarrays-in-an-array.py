class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        

        l = 0
        arr = 0
        counts = defaultdict(int)
        k = len(set(nums))
        N = len(nums)
        for r, n in enumerate(nums):
            counts[n] += 1

            while len(counts) == k:
                counts[nums[l]] -= 1
                if counts[nums[l]] == 0:
                    del counts[nums[l]]
                l += 1
                arr += N - r

        
        return arr