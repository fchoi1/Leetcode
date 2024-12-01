class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for n in arr:
            if (n % 2 == 0 and n // 2 in seen) or n * 2 in seen:
                return True
            seen.add(n)
        return False
        