class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numSet = set(nums)

        result = []
        N = len(nums)
        def generate(numSet, currList):
            if len(currList) >= N:
                result.append(currList)
                return
            
            for n in numSet:
                newSet = set(numSet)
                newSet.remove(n)
                newList = currList[:]
                newList.append(n)
                generate(newSet, newList)

        generate(numSet, [])
        return result
        