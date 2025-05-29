class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        adj1 = defaultdict(set)
        adj2 = defaultdict(set)

        for a,b in edges1:
            adj1[a].add(b)
            adj1[b].add(a)

        for a,b in edges2:
            adj2[a].add(b)
            adj2[b].add(a)

        def countNodes(node, adj):
            odd = set()
            even = set()
            def dfs(parent, child, isEven):
                for nextNode in adj[child]:
                    if nextNode == parent:
                        continue
                    dfs(child, nextNode, not isEven)

                if isEven:
                    even.add(child)
                else:
                    odd.add(child)

            dfs(None, node, False)
            return (odd, even)

        odd_1, even_1 = countNodes(0, adj1)
        odd_2, even_2 = countNodes(0, adj2)

        max_m = max(len(odd_2), len(even_2))
        o_1 = len(odd_1)
        e_1 = len(even_1)

        ans = []
        for i in range(n):
            if i in odd_1:
                ans.append(o_1 + max_m)
            else:
                ans.append(e_1 + max_m)

        return ans

        
