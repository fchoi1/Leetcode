class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            for char in str(n):
                ans.append(int(char))

        return ans