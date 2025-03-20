    

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        parent = {i:i for i in range(n)} 
        size = defaultdict(int)
        weights = {}

        def find(node):

            if node == parent[node]:
                return node
            return find(parent[node])
   
        def union(n1, n2, weight):
            r1 = find(n1)
            r2 = find(n2)

            if r1 in weights:
                weight &= weights[r1]
            if r2 in weights:
                weight &= weights[r2]

            weights[r1] = weight
            weights[r2] = weight

            if r1 == r2:
                return
            
            if size[r1] > size[r2]:
                parent[r2] = r1
                size[r1] += 1
            else:
                parent[r1] = r2
                size[r2] += 1
        
        weights = {}

        for a,b,w in edges:
            union(a,b,w) 
            
        ans = []
        for start,end in query:
            
            r1 = find(start)
            r2 = find(end)
            
            if r1 != r2:
                ans.append(-1)
            else:
                ans.append(weights[r1])
        
        return ans
