class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        # get path of node1

        # get path of node 2 done return first node that intersects on path 2

        p1 = {}

        curr = node1
        dist = 0
        while curr != -1 and curr not in p1:
            p1[curr] = dist
            dist += 1
            curr = edges[curr]

        p2 = set()
        curr = node2
        dist = 0

        min_dist = inf
        min_node = inf
        while curr != -1 and curr not in p2:
            if curr in p1:
                max_dist = max(dist, p1[curr])
                if max_dist < min_dist:
                    min_dist = max_dist
                    min_node = curr
                elif max_dist == min_dist:
                    min_node = min(min_node, curr)


            p2.add(curr)
            curr = edges[curr]
            dist += 1
        return min_node if min_node != inf else -1