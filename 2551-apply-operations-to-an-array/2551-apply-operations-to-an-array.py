class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        arr = []
        i = 0

        while i < N:
            if nums[i] == 0:
                i += 1
                continue
            if i < N - 1 and nums[i] == nums[i + 1]:
                arr.append(nums[i] * 2)
                i += 2
            else:
                arr.append(nums[i])
                i += 1
        
        while len(arr) != N:
            arr.append(0)
        
        return arr
        