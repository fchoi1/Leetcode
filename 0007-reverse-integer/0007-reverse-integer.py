class Solution:
    def reverse(self, x: int) -> int:
        newInt = -int(str(abs(x))[::-1]) if x < 0 else int(str(abs(x))[::-1])
        return newInt if -2**31 <= newInt <= 2**31-1 else 0
