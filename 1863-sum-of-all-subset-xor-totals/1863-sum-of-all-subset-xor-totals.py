class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.sum = 0 
        def traverse(index, val):
            self.sum += val
            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                val ^= nums[i]
                traverse(i + 1, val)
                val ^= nums[i]
        
        traverse(0, 0)
        return self.sum