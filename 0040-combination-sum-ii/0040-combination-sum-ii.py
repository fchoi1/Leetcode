class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(index, currSum, arr):
            if currSum > target:
                return
            if currSum == target:
                res.append(arr[:])

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                arr.append(candidates[i])
                backtrack(i+1, currSum + candidates[i], arr)
                arr.pop()

        backtrack(0,0,[])

        return res
        