class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def validPart(index, numList, curr, target):
            if index >= len(numList) or curr > target:
                return curr == target
            currStr = ''
            for i in range(index, len(numList)):
                currStr += str(numList[i])
                if validPart(i + 1, numList, curr + int(currStr), target):
                    return True
            return False

        ans = 0
        for i in range(n + 1):
            square = i * i
            if validPart(0, list(map(int, str(square))), 0, i):
                ans += square
        return ans

