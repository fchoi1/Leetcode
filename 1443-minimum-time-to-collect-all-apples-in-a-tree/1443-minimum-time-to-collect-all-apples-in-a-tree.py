class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        adjMap = defaultdict(list)
        for a,b in edges:
            adjMap[a].append(b)
            adjMap[b].append(a)


        seen = set()

        # returns length of 1 if it is an apple, else 0
        def getPath(node):
            

            if node in seen:
                return 0
            
            seen.add(node)

            path = 2 if hasApple[node] and node != 0 else 0
            childPath = 0

            for nextNode in adjMap[node]:
                if nextNode in seen:
                    continue
                childPath += getPath(nextNode)

            if childPath != 0 and not hasApple[node] and node != 0:
                path += 2
    
            print(node, "total path", path + childPath)
            return path + childPath


            # check if child has apple
            # root?
        
        return getPath(0)