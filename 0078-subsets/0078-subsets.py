class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        unique = []
        def backtrack(index, currArray):
            unique.append(currArray[:])
            if index >= len(nums):
                return
            
            for i,n in enumerate(nums[index:]):
                currArray.append(n)
                backtrack(index + 1 + i, currArray)
                currArray.pop()
                
        backtrack(0, [])
        return unique

        