class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        currA = set()
        currB = set()
        curr = set()
        ans = []
        for a_n, b_n in zip(A,B):
            currA.add(a_n)
            currB.add(b_n)

            if a_n in currB:
                curr.add(a_n)
            if b_n in currA:
                curr.add(b_n)
            ans.append(len(curr))
        return ans

        