class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # move at most k

        # sorted

        startTime.sort()
        endTime.sort()
        N = len(startTime)
        # heap or sliding window?
        prevE = 0
        maxFree = 0
        for i in range(k + 1):
            if i >= N:
                return maxFree + eventTime - prevE
            s,e = startTime[i], endTime[i]

            maxFree += s - prevE
            prevE = e

        print("curr Max", maxFree)
        # ...1.1.1


        firstS = s
        firstE = endTime[0]
        currFree = maxFree
        for i in range(k + 1, N + 1):

            firstS = startTime[i - k - 1]
            firstE = endTime[i - k - 2] if i - k - 2 >= 0 else 0

            if i >= N:
                currFree += eventTime - prevE
                currFree -= firstS - firstE
                print("END", currFree, maxFree, "add", eventTime - prevE, "sub", firstS - firstE, (firstS,firstE))
                return max(maxFree, currFree)

            s,e = startTime[i], endTime[i]
            
            currFree -= firstS - firstE

            currFree += s - prevE
            print("prevS", firstS, firstE, currFree, "add", s - prevE, 'sub', firstS - firstE)
            maxFree = max(maxFree, currFree)
            
            prevE = e
        # shouldn't reach?
        return maxFree

