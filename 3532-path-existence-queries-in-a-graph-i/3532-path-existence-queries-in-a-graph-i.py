class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # build the graph


        # run dfs for cc (union find)

        # sliding window

        cc = [None] * (n + 1)
        curr = 0
        q = deque([])

        for i, val in enumerate(nums):
            while q and val - q[0] > maxDiff:
                q.popleft()
            if not q:
                curr += 1
        
            q.append(val)
            cc[i] = curr
            
             
        print(cc)
        return [cc[a] == cc[b] and (cc[a] != None or cc[b] != None) for a,b in queries]

