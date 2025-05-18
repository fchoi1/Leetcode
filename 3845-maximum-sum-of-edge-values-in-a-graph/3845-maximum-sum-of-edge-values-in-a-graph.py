class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        # O(NLogN+E)
        adj = defaultdict(set)

        for a,b in edges:
            adj[a].add(b)
            adj[b].add(a)

        curr = 1
        seen = set()
        single = []
        for node in adj:
      
            if len(adj[node]) == 1 and node not in seen:
                
                link = 1
                currNode = node
                temp = set()
                while currNode not in temp:
                    temp.add(currNode)
                    for i in adj[currNode]:
                        if i not in temp:
                            currNode = i
                            break
                single.append(len(temp))
                seen |= temp
                
        loops = []
        for node in adj:
            if node in seen:
                continue
                
            link = 1
            currNode = node
            temp = set()
            while currNode not in temp:
                temp.add(currNode)
                for i in adj[currNode]:
                    if i not in temp:
                        currNode = i
                        break
            loops.append(len(temp))
            seen |= temp


        loops.sort()
        single.sort(reverse=True)     


        l_idx = 0
        s_idx = 0
        ans = 0
        i = n
        while i >= 1:

            if l_idx >= len(loops) and s_idx >= len(single):
                break

            loop_count = loops[l_idx] if l_idx < len(loops) else single[s_idx]
            is_loop =  l_idx < len(loops)
            h = []

            for _ in range(loop_count):
                curr = i
                            
                if not h:
                    heapq.heappush(h, (-i, 2))
                else:
                    highest, times = heapq.heappop(h)
                    while times == 0:
                        highest, times = heapq.heappop(h)
                        
                    ans += -highest * curr
                    if times > 1:
                        heapq.heappush(h, (highest, times-1))

                    heapq.heappush(h,(-i,1))
                i -= 1
            if is_loop:
                ans += (i+1) * -h[0][0]
                l_idx +=1
            else:
                s_idx += 1

        return ans
                
                




        