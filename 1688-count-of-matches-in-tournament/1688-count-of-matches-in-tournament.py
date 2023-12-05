class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        def countMatch(n, games):
            if n == 1:
                return games
            return countMatch(math.ceil(n/2), games+n//2)
        return countMatch(n,0)
        