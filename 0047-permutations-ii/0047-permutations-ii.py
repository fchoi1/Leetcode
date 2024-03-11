class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(arr, n , seen):
            if len(arr) == len(nums):
                res.add(tuple([i for i in arr]))
            
            for i,val in enumerate(nums):
                if i in seen:
                    continue
                arr.append(val)
                seen.add(i)
                dfs(arr, n + 1, seen)
                arr.pop()
                seen.remove(i)
        dfs([], 0, set())
        return res
        