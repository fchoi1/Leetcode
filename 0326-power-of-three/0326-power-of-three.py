
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        log_val = math.log(n, 3)
        print(log_val)
        return math.isclose(log_val, round(log_val), rel_tol=1e-12)