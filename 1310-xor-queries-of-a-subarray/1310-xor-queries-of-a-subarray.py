class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = []
        val = 0
        ans = []
        for n in arr:
            val ^= n
            prefix.append(val)

        for l,r in queries:
            if l == 0:
                ans.append(prefix[r])
            else:
                ans.append(prefix[r] ^ prefix[l-1])
        
        return ans