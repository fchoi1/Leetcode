class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(arr, seen):
            if len(arr) == len(nums):
                res.add(tuple([i for i in arr]))
            
            for i,val in enumerate(nums):
                if i in seen:
                    continue
                seen.add(i)
                dfs(arr + [val], seen)
                seen.remove(i)
        dfs([],0, set())
        return res
        