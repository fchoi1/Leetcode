class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = 0
        prevLasers = bank[0].count('1')    
        for row in bank[1:]:
            if int(row) == 0:
                continue
            currLasers = row.count('1')
            lasers += currLasers* prevLasers
            prevLasers = currLasers
        return lasers
        