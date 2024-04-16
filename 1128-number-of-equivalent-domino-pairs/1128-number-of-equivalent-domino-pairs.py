class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        dMap = defaultdict(int)
        for pair in dominoes:
            if tuple(pair) in dMap:
                count += dMap[tuple(pair)] 
                dMap[tuple(pair)] += 1
            elif tuple(pair[::-1]) in dMap:
                count +=  dMap[tuple(pair[::-1])]
                dMap[tuple(pair[::-1])] += 1
            else:
                dMap[tuple(pair)] = 1
        return count 
        