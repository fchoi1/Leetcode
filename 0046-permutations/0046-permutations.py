class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.ans = []
        N = len(nums)

        def backtrack(currList, seen):
            if len(currList) == N:
                self.ans.append(currList[::])
                return

            for i, n in enumerate(nums):
                if i not in seen:
                    seen.add(i)
                    backtrack(currList + [n], seen)
                    seen.remove(i)
                    
        backtrack([], set())
        return self.ans
