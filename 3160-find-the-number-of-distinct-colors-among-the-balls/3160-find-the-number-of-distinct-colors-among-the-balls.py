class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        colors = {}
        ballMap = {}
        ans = []

        for x,y in queries:

            if x in ballMap and ballMap == y:
                continue

            if x in ballMap:
                colors[ballMap[x]] -= 1
                if colors[ballMap[x]] == 0:
                    del colors[ballMap[x]]
            ballMap[x] = y


            if y not in colors:
                colors[y] = 0
                
            colors[y] += 1

            ans.append(len(colors))

        return ans