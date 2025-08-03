class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:

        idx = -1
        for pos, f in fruits:
            if pos > startPos:
                break
            idx += 1

        N = len(fruits)
        
        l = idx
        r = idx + 1

        # go left 
        currFruits = 0
        while l >= 0 and (startPos - fruits[l][0]) <= k:
            currFruits += fruits[l][1]
            l -= 1
        l += 1
        maxFruits = currFruits

        # go right 
        while r < N and (fruits[r][0] - startPos) <= k:

            currSteps = (fruits[r][0] - startPos)

            backforth = min((startPos - fruits[l][0] + currSteps * 2), ((startPos - fruits[l][0]) * 2 + currSteps))

            while l <= idx and backforth > k:
                currFruits -= fruits[l][1]
                l += 1
                backforth = min((startPos - fruits[l][0] + currSteps * 2), ((startPos - fruits[l][0]) * 2 + currSteps))

            currFruits += fruits[r][1]
            maxFruits = max(maxFruits, currFruits)
            r += 1

        return maxFruits