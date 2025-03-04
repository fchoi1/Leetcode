class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        index = 0
        arr = []
        while (3 ** index) <= 10 ** 7:
            arr.append(3 ** index)
            index += 1
        arr.append(3 ** index)
        
        def backtrack(currSum, index):
            if currSum > n or index >= len(arr):
                return False
            if currSum == n:
                return True


            for i in range(index, len(arr)):
                if currSum + arr[i] > n:
                    break
                if backtrack(currSum + arr[i], i + 1):
                    return True
            return False

        return backtrack(0, 0)