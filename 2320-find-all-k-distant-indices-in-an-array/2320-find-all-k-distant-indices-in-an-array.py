class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        # two passes
        count = -1
        validK = set()
        for i, val in enumerate(nums):
            if val == key:
                count = k 
            
            if count >= 0:
                validK.add(i)
                count -= 1

        N = len(nums)
        count = -1
        for i, val in enumerate(nums[::-1]):
            if val == key:
                count = k
            if count >= 0:
                validK.add(N - i - 1)
                count -= 1
                
        return list(validK)

        