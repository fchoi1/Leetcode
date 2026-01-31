class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # binary seach
        N = len(letters)
        l = 0
        r = N - 1

        while l < r:
            mid = (l + r) // 2

            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid

        return letters[l] if letters[l] > target else letters[0]