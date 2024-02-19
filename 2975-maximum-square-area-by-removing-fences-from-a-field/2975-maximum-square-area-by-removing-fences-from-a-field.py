class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        maxArea = -1
        pairs = set()
        hFences.extend([1,m]), vFences.extend([1,n])
        hFences.sort(), vFences.sort()
        for i, h1 in enumerate(hFences[:-1]):
            for h2 in hFences[i+1:]:
                pairs.add(h2-h1)
        for i, v1 in enumerate(vFences[:-1]):
            for v2 in vFences[i+1:]:
                if (v2-v1)in pairs:
                    maxArea = max(maxArea,(v2-v1)**2)
        if maxArea == -1:
            return -1
        return maxArea % (10**9 + 7)