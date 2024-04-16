class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        dMap = defaultdict(int)
        for a,b in dominoes:
            pair = (min(a,b), max(a,b))
            if pair in dMap:
                count += dMap[pair] 
                dMap[pair ] += 1
            else:
                dMap[pair ] = 1
        return count 
        