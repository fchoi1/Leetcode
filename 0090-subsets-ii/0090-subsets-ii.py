class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        combos = []
        nums.sort()

        def backtrack(index, arr):
            combos.append(arr[:])
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                # if curr element equal prev, skip
                if i > index and nums[i] == nums[i-1]:
                    continue
                arr.append(nums[i])
                backtrack(i+1, arr)
                arr.pop()
              
        backtrack(0,[])
        return combos