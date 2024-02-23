class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numMap = set()
        for n in arr:
            if n in numMap:
                return True
            numMap.add(n*2)
            if n % 2 == 0:
                numMap.add(n // 2)
        return False        