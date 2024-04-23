class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        minList = []
        adjMap = defaultdict(set)

        def getHeight(node, seen, path):
            nonlocal longest
            if node in seen:
                if len(path) > len(longest):
                    longest = path.copy()
                return
            path.append(node)
            seen.add(node)
            for nextNode in adjMap[node]:
                getHeight(nextNode, seen, path)
            seen.remove(node)
            path.pop()
   
        for a,b in edges:
            adjMap[a].add(b)
            adjMap[b].add(a)
        
        longest = []
        getHeight(0, set(),[])
        print(longest)

        getHeight(longest[-1], set(), [])
        print(longest, len(longest) )
        
        mid = len(longest) // 2
        if len(longest) % 2 == 0:
            return longest[mid-1: mid+1] 

        return [longest[mid]]
        
        
        