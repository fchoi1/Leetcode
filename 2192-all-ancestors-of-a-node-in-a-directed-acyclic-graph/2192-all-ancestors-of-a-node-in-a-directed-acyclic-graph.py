class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    
        def getNode(node):
            if node in self.cache:
                return self.cache[node]
            arr = []
            for nextNode in self.nodes[node]:
                next_arr = getNode(nextNode)
                arr.append(nextNode)
                arr.extend(next_arr)
                    
            # print("done ", node, arr)
            sorted_arr = sorted(list(set(arr)))
            self.cache[node] = sorted_arr
            return sorted_arr

        self.nodes = {}
        for i in range(n):
            self.nodes[i] = []

        for a,b in edges:
            self.nodes[b].append(a)

        ans = []
        self.cache = {}
        for i in range(n):
            ans.append(getNode(i))
        print(self.cache, self.nodes)
        return ans
        
      

        