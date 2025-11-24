class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        curr = 0
        for b in nums:
            curr = (curr << 1) | b
            ans.append(curr % 5 == 0)
        
        return ans