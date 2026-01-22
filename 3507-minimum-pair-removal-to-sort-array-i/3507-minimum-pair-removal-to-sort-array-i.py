class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        

        isSorted = False

        ops = 0
        while not isSorted:
            minVal = inf
            idx = -1
            isSorted = True
            for i, (prev, curr) in enumerate(zip(nums, nums[1:])):
                if prev + curr < minVal:
                    idx = i
                    minVal = prev + curr
                
                if prev > curr:
                    isSorted = False
            
            if isSorted:
                break

            ops += 1

            arr = []
            for i, n in enumerate(nums):
                if i == idx:
                    arr.append(minVal)
                elif i == idx + 1:
                    continue
                else:
                    arr.append(n)
                    
            nums = arr
        
        return ops