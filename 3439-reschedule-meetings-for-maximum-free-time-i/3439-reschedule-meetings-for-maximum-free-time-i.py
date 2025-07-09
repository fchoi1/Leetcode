class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

        N = len(startTime)
        prevE = maxFree = 0
        for i in range(k + 1):
            if i >= N:
                return maxFree + eventTime - prevE
            s,e = startTime[i], endTime[i]

            maxFree += s - prevE
            prevE = e

        currFree = maxFree
        for i in range(k + 1, N + 1):

            firstS = startTime[i - k - 1]
            firstE = endTime[i - k - 2] if i - k - 2 >= 0 else 0

            # End condition
            if i >= N:
                currFree += eventTime - prevE
                currFree -= firstS - firstE
                return max(maxFree, currFree)

            s,e = startTime[i], endTime[i]
        
            currFree -= firstS - firstE
            currFree += s - prevE
            prevE = e

            maxFree = max(maxFree, currFree)
            

        # shouldn't reach ever
        return maxFree

