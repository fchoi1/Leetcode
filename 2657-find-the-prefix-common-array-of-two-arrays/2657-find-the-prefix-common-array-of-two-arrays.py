class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        ans = []

        currA = defaultdict(int)
        currB = defaultdict(int)

        for a,b in zip(A,B):
            currA[a] += 1
            currB[b] += 1

            common = 0
            for k,v in currA.items():
                common += min(v, currB[k])
            
            ans.append(common)
        return ans
                