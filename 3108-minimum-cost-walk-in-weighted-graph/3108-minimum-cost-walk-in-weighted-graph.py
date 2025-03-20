    

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        parent = {i:i for i in range(n)} # key: rep and wieght
        size = defaultdict(int)
        weights = {}

        def find(node):
       
            while node != parent[node]:
                # compress
                parent[node] = parent[parent[node]]
                node = parent[node]
            
            return parent[node]
        
        def union(n1, n2, weight):
            r1 = find(n1)
            r2 = find(n2)

            print("\nunion", n1, n2, weight)
            if r1 in weights:
                weight &= weights[r1]
            if r2 in weights:
                weight &= weights[r2]

            # already same
            if r1 == r2:
                weights[r1] = weight
                return
            
            # set larger as parent  
            if size[r1] > size[r2]:
                parent[r2] = r1
                weights[r1] = weight
                size[r1] += 1
            else:
                parent[r1] = r2
                weights[r2] = weight
                size[r2] += 1
        


        # Dijstras? bfs
        # priority q

        # preprocess?
        

        # groups?
        adj = defaultdict(set)
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
