class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        maxArea = 1

        # check max in a row to remove from each direction

        hBars.sort()
        vBars.sort()

        def countConsecutive(arr):
            maxCount = count = 1
            for prev, curr in zip(arr, arr[1:]):
                if curr == prev + 1:
                    count += 1
                else:
                    count = 1
                maxCount = max(maxCount, count)

            return maxCount

        
        hCount = countConsecutive(hBars)
        vCount = countConsecutive(vBars)
        return (min(hCount, vCount) + 1) ** 2
