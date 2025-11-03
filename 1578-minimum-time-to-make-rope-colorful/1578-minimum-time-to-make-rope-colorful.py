class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:


        N = len(colors)
        prev = colors[0]
        i = 1
        currSum = currMax = neededTime[0]
        total = 0

        while i  < N:
            curr = colors[i]
            if prev != curr:
                total += currSum - currMax
                currSum = currMax = 0

            currMax = max(currMax, neededTime[i])
            currSum += neededTime[i]
            prev = curr
            i += 1

        return total + currSum - currMax


