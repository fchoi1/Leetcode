class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        sol = []
        N = len(candidates)
        def backtrack(index, arr, currSum):
            nonlocal sol,N

            if currSum >= target  or index >= N:
                if currSum > target:
                    return
                if currSum == target:
                    sol.append(arr[:])

            for i in range(index, N):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                arr.append(candidates[i])
                backtrack(i + 1, arr, currSum + candidates[i])
                arr.pop()
        
        backtrack(0,[],0)
        return sol
            
            
                