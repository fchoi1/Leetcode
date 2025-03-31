class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n_set = defaultdict(int)
        count = 0
        # backwards calculate from r
        for r in range(4, len(nums) - 2):

            q = r - 2
            for p in range(q-1):
                n_set[nums[p]/nums[q]] += 1  

            for s in range(r + 2, len(nums)):
                count += n_set[nums[s]/nums[r]]

        return count

        
        