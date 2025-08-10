class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 9 digits?
        # backtrack

        nSet = Counter(str(n))
        N = len(str(n))
        
        def backtrack(numCount, n):
            if sum(v for v in numCount.values()) == 0:
                return bin(int(n)).count('1') == 1
            
            for val, count in numCount.items():
                if len(n) == 0 and val == '0' or count == 0:
                    continue
                numCount[val] -= 1
                if backtrack(numCount, n + val):
                    return True
                numCount[val] += 1
            return False

        return backtrack(nSet, '')