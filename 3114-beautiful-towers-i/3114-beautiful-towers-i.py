class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def generatePrefixSum(hieghts: List) -> List:
            prefixList = []
            stack = []
            prev = hieghts[0]
            for i,h in enumerate(hieghts):
                if h >= prev:
                    prefixList.append(h) if not prefixList else prefixList.append(h + prefixList[-1])
                else:
                    while h < prev:
                        if not stack:
                            prev = h
                            index = None
                            break
                        prev, index = stack.pop()
                    if index != None:
                        stack.append((prev,index)) # add back index into stack (new min)
                        prefixList.append(h*(i-index) + prefixList[index])
                    else:
                        prefixList.append(h*(i+1))
                prev = h
                stack.append((h,i))
            return prefixList

        N = len(maxHeights)
        forward = generatePrefixSum(maxHeights)
        backward = generatePrefixSum(maxHeights[::-1])
        backward.reverse()
        maxSum = forward[-1]
        for i in range(N):
            maxSum = max(maxSum, backward[i] if i == 0 else forward[i - 1] + backward[i])
        return maxSum
            
        