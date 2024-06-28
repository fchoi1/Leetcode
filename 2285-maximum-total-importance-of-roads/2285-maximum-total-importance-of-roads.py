class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        nodes = defaultdict(int)
        for a,b in roads:
            nodes[a] += 1
            nodes[b] += 1
        
        node_order = [a for a,b in sorted(nodes.items(), key=lambda x: x[1], reverse=True)]

        node_map = {}
        for node in node_order:
            node_map[node] = n
            n -= 1
        val = 0

        for a,b in roads:
            val += node_map[a] + node_map[b]
        return val
        