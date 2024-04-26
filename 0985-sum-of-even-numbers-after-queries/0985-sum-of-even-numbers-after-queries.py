class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        currSum = sum([n if n % 2 == 0 else 0 for n in nums])
        for val, index in queries:
            if nums[index] % 2 == 0:
                currSum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                currSum += nums[index]
            ans.append(currSum)
        return ans
            

        