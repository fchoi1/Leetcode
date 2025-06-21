class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        maxDist = 0
        currCount = defaultdict(int)
        for d in s:
            currCount[d] += 1
            maxVert, minVert = max(currCount['N'], currCount['S']), min(currCount['N'], currCount['S'])
            maxHor, minHor = max(currCount['W'], currCount['E']), min(currCount['W'], currCount['E'])
            
            diff = min(k, minVert + minHor)
            maxDist = max(maxDist, maxVert + maxHor - minVert - minHor + 2 * diff)
        return maxDist