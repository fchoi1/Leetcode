class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        adj = defaultdict(set)
        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)

        # bfs

        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)

        q = deque([(0, 1)])
        while q:
            curr_time, node = q.popleft()

            if node == n and dist1[node] != -1 and curr_time != dist1[node]:
                return curr_time

            if dist1[node] == -1:
                dist1[node] = curr_time
            elif dist2[node] == -1 and curr_time != dist1[node]:
                dist2[node] = curr_time
            else:
                continue
            

            if (curr_time // change) % 2 == 1: # red
                curr_time = ((curr_time // change) + 1) * change
                
            for next_node in adj[node]:
                q.append((curr_time + time, next_node))
        print(dist1[n], dist2[n])
        return dist2[n]

      