class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for a,b,c in zip(arr, arr[1:], arr[2:]):
            if all(n % 2 == 1 for n in [a,b,c]):
                return True
        return False