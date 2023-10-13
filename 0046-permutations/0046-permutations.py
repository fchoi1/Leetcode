class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numSet = set(nums)
        result = []
        def generate(currList):
            if len(currList) >= len(nums):
                result.append(currList[:])
                return
            
            for n in nums:
                if n not in currList:
                    currList.append(n)
                    generate(currList)
                    currList.pop()

        generate([])
        return result
        