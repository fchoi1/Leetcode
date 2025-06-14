class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxNum = num
        minNum = num

        for i in range(10):
            for j in range(10):
                maxNum = max(maxNum, int(str(num).replace(str(i), str(j))))
                minNum = min(minNum, int(str(num).replace(str(i), str(j))))
        return maxNum - minNum