class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        self.terminal = set()
        
        def dfs(node,seen):
            if node in self.terminal:
                return True

            if node in seen:
                return False
    
            seen.add(node)
            for nextNode in graph[node]:
                isDag = dfs(nextNode, seen)
                # print("next", nextNode, isDag, seen)
                if not isDag:
                    return False

            self.terminal.add(node)
            return True

    
        for i in range(len(graph)):
            if i in self.terminal:
                continue
            isDag = dfs(i, set())
     
            
        return sorted(list(self.terminal))