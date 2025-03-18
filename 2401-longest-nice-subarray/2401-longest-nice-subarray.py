class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # 110000
        # 001000
        # 000011

        # arr of 30, need each to be only 1, else keep going

        arr = [0] * 30

        prefix = []
        curr =  0xffffffff
        l = 0
        maxLen = 1


        def isValid(arr):
            return all(c < 2 for c in arr)
        
        def applyBin(n, arr, subtract):
            binary = bin(n)[2:].zfill(30)
            for i,c in enumerate(binary):
                if c == '1':
                    if subtract:
                        arr[i] -= 1
                    else:
                        arr[i] += 1
            return arr

        for r,n in enumerate(nums):

            arr = applyBin(n, arr, False)
            
            while not isValid(arr) and l <= r:
                arr = applyBin(nums[l], arr, True)
                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen