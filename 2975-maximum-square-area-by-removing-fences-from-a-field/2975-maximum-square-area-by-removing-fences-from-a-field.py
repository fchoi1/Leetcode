class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # get the various lengths of the hFennces
        hFences.sort()
        vFences.sort()

        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]
        

        hLengths = set()
        for i, h1 in enumerate(hFences):
            for h2 in hFences[i+1:]:
                hLengths.add(h2 - h1) 
        
        maxArea = -1
        mod = 10 ** 9 + 7
        for i, v1 in enumerate(vFences):
            for v2 in vFences[i+1:]:
                if (v2 - v1) in hLengths:
                    maxArea = max(maxArea, ((v2 - v1) ** 2))
        
        return -1 if maxArea == -1 else maxArea % mod 