class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        # prime it always odd
        # 
        for n in nums:
            for x in range(n):
                if x | x + 1 == n:
                    ans.append(x)
                    break
            else:
                ans.append(-1)
        return ans
