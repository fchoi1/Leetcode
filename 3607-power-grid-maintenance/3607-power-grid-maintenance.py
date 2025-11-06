class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:

        # groups or sets

        # process connections

        stations = {} # group id, online 
        groups = [] # list of heaps

        adj = defaultdict(set)

        for a,b in connections:
            adj[a].add(b)
            adj[b].add(a)

        group_id = 0

        for i in range(1, c + 1):
            
            # new group
            if i not in stations:
                group_id = len(groups)
                #  bfs to get groups
                group = []
                q = [i]
                while q:
                    t = []
                    for node in q:
                        if node in stations:
                            continue
                        
                        heappush(group, node)

                        # assign nodes
                        stations[node] = (group_id, True)

                        for n in adj[node]:
                            t.append(n)
                    q = t
                groups.append(group)
        
        # process queries
        ans = []
        for a, s in queries:
            g_id, is_active = stations[s]
            if a == 2:                
                stations[s] = (g_id, False)
            else:
                if is_active:
                    ans.append(s)
                    continue

                # pop if station is inactive
                while groups[g_id] and not stations[groups[g_id][0]][1]:
                    heappop(groups[g_id])

                if groups[g_id]:
                    ans.append(groups[g_id][0])
                else:
                    ans.append(-1)


        return ans




        