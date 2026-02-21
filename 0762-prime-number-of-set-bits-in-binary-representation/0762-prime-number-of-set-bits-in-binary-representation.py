class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        prime = set([2,3,5,7,11,13,17,19,23])
        count = 0
        
        for n in range(left, right + 1):
            ones = bin(n).count('1')

            if ones in prime:
                count += 1
        
        return count
