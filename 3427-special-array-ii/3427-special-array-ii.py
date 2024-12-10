class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        count = 0
        prev = None
        prefix = []
        for n in nums:
            if prev and (prev + n) % 2 == 0:
                count += 1
            prefix.append(count)
            prev = n

        ans = []
        for a,b in queries:
            ans.append(prefix[a] == prefix[b])
        return ans