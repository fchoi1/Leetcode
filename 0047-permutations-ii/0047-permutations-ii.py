class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        seen = set()
        N = len(nums)

        def dfs(arr):
            if len(arr) == N:
                res.add(tuple([i for i in arr]))
            
            for i,val in enumerate(nums):
                if i in seen:
                    continue
                seen.add(i)
                dfs(arr + [val])
                seen.remove(i)
        dfs([])
        return res
        