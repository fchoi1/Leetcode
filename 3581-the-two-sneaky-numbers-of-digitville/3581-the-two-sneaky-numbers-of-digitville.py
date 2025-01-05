class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        digits = [0] * len(nums)
        sneaky = []
        for n in nums:
            digits[n] += 1
            if digits[n] == 2:
                sneaky.append(n)
                if len(sneaky) == 2:
                    return sneaky