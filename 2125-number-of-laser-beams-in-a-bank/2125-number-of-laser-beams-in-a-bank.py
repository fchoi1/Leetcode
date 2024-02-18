class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = 0
        prevLasers = sum(x == '1' for x in bank[0])        
        for row in bank[1:]:
            if int(row) == 0:
                continue
            currLasers = sum(x == '1' for x in row) 
            lasers += currLasers* prevLasers
            prevLasers = currLasers
        return lasers
        