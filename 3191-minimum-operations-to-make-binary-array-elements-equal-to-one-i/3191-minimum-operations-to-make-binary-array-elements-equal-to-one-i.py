class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # greedy approach?

        i = 0
        N = len(nums)
        flip = 0
        while i < len(nums):
            if not nums[i]:
                flip += 1
                nums[i] = 1
                if i + 2 < N:
                    nums[i + 1] ^= 1
                    nums[i + 2] ^= 1
                
                else:
                    return -1
                #fliip
            i += 1

        # 0 1 1 1 0 1 
        # 1 0 0 1 0 1
        # 1 1 1 0 1 0
        # 1 1

        # 0,1,1,1,0,0
        # 1 0 0 1 0 0
        # 1 1 1 0 0 0
        # 1 1 1 1 1 1
        print(nums)
        return flip