class Solution:
    def maximumSwap(self, num: int) -> int:
        strNum = str(num)
        N = len(strNum)
        maxVal = [None for _ in range(N)]

        currMax = int(strNum[-1])
        currIndex = N - 1
        
        # reverse check
        for i in range(N-1, -1, -1):
            if int(strNum[i]) > currMax:
                currMax = int(strNum[i])
                currIndex = i
            maxVal[i] = (currMax,currIndex)

        strNum = ""
        skip = swap = None
        for i,n in enumerate(str(num)):
            
            if i == skip:
                strNum += swap
                continue

            currMax, currIndex = maxVal[i]
            if int(n) < currMax and swap == None:
                strNum += str(currMax)
                skip = currIndex
                swap = n
                continue
            
            strNum += n
        
        return int(strNum)

      