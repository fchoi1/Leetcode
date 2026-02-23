class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

    
        curr = s[:k]
        subSet = set([curr])
        for i in range(k, len(s)):
            curr = curr[1:]
            curr += s[i]
            subSet.add(curr)
        return len(subSet) == (2 ** k)


        # for i in range(2 ** k):
        #     binStr = bin(i)[2:].zfill(k)
        #     if binStr not in subSet:
        #         return False
        # return True