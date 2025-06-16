class Solution:
    def maxDiff(self, num: int) -> int:

        maxNum = num
        minNum = num

        for i in range(10):
            for j in range(10):
                newNum = int(str(num).replace(str(i), str(j)))

                if len(str(newNum)) != len(str(num)) or newNum == 0:
                    continue
                maxNum = max(maxNum, newNum)
                minNum = min(minNum, int(str(num).replace(str(i), str(j))))

        return maxNum - minNum