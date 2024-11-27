class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        paths = {x: {x+1} for x in range(n)}

        def bfs(paths):
            q = [0]
            steps = 0
            seen = set()
            while q:
                temp = []
                for i in q:
                    if i == n:
                        return steps - 1
                    if i in seen:
                        continue
                    seen.add(i)
                    for nextNode in paths[i]:
                        temp.append(nextNode)
                steps += 1
                q = temp
            return -1

        ans = []
        for a,b in queries:
            paths[a].add(b)
            ans.append(bfs(paths))
        return ans


