class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # join at the middle for each
        # find longest path of a tree

        # combine the longest 2 paths

        def getMap(edges):
            adj = defaultdict(set)
            for a,b in edges:
                adj[a].add(b)
                adj[b].add(a)
            return adj

        adj1 = getMap(edges1)
        adj2 = getMap(edges2)

        def getLongest(node, length, adj, seen):
            if node in seen:
                return length, node
            seen.add(node)
            l = 0
            furthest = None
            for n in adj[node]:
                currLen, currNode = getLongest(n, length+1, adj, seen)
                if currLen > l:
                    l = currLen
                    furthest = currNode
            return l, furthest
        
        def get2Longest(adj):
            _, A = getLongest(0,0,adj, set())
            longest, _ = getLongest(A,0,adj, set())
            return longest

        l1 = get2Longest(adj1)
        l2 = get2Longest(adj2)
    
        short = min(l1, l2)
        longer = max(l1, l2)
        if short < ceil(longer / 2):
            return longer
        return max(longer, ceil(longer/2) + ceil((short)/2) + 1)



