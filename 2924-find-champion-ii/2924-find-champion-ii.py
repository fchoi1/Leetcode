class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # find nodes without incoming
        weak = set()

        for a,b in edges:
            weak.add(b)

        if n - len(weak) > 1:
            return -1

        i = 0
        while i in weak:
            i += 1
        return i