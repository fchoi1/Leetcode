class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        seen = set()
        def dfs(arr):
            if len(arr) == len(nums):
                res.add(tuple([i for i in arr]))
            
            for i,val in enumerate(nums):
                if i in seen:
                    continue
                seen.add(i)
                dfs(arr + [val])
                seen.remove(i)
        dfs([])
        return res
        