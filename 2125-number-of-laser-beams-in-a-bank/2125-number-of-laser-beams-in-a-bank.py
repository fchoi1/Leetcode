class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        prev = bank[0].count('1')
        total = 0
        for b in bank[1:]:
            curr = b.count('1')
            if curr == 0:
                continue
            total += prev * curr 
            prev = curr
        return total
        