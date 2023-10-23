class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(currSum, combo, index):
            if currSum > target:
                return
            
            if currSum == target:
                res.append(combo[:])
                return

            for i, n in enumerate(candidates[index:]):
                currSum += n
                combo.append(n)
                backtrack(currSum, combo, index + i)
                combo.pop()
                currSum -= n
        backtrack(0,[],0)
        print("res", res)
        return res
       
