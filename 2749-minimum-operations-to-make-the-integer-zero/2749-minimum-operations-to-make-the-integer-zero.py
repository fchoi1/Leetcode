class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        # ops * n2 

        ops = 1

        while True:
            target = num1 - num2 * ops

            if ops > target:
                return -1
            
            if ops >= target.bit_count():
                break
            ops += 1


        return ops
        