class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        # bubble sort
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                bit_i = bin(nums[i]).count('1')
                bit_j = bin(nums[j]).count('1')
                if nums[i] > nums[j]:
                    if bit_i == bit_j:
                        nums[j], nums[i] = nums[i], nums[j]
                    else:
                        break
        prev = None
        for n in nums:
            if prev and n < prev:
                break
            prev = n
        else:
            return True
        return False
