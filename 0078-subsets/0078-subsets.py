class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        combos = []

        def backtrack(index, array):
            combos.append(array[:])
            if index == len(nums):
                return
            for i,n in enumerate(nums[index:]):
                array.append(n)
                backtrack(i + index + 1, array)
                array.pop()
        backtrack(0, [])
        
        return combos
        