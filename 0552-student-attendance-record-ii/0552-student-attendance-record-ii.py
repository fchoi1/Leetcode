class Solution:
    def checkRecord(self, n: int) -> int:
        cache = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]
        mod = 10 ** 9 + 7
        
        def generate(length, absent, lates):
            if cache[length][absent][lates] != -1:
                return cache[length][absent][lates]
            if absent >= 2 or lates >= 3:
                return 0
            if length == 0:
                return 1

            val = generate(length-1, absent, 0)
            if absent == 0:
                val += generate(length-1, absent + 1, 0)
            if lates < 2:
                val += generate(length-1, absent, lates + 1)

            cache[length][absent][lates] = val % mod 
            return cache[length][absent][lates] 

        return generate(n, 0, 0)