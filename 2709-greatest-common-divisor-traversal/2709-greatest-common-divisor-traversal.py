class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        nodes = {}
        filtered = set(nums)
        if len(filtered) == 1:
            if len(nums) > 1:
                return nums[0] != 1
            return True
        # get primes for each (preprocess)
        N = max(filtered)
        prime_divs = [[i] for i in range(N+1)]
        prime_divs[1] = [] # 1 has no prime divisors
        for p in range(2, N+1):
            if len(prime_divs[p]) == 1:
                for i in range(p, N+1, p):
                    prime_divs[i].append(p)
        for i, n in enumerate(filtered):
            for prime in prime_divs[n]:
                if n not in nodes:
                    nodes[n] = Node(n)
                if prime not in nodes:
                    nodes[prime] = Node(prime)
                nodes[n].neighbors.append(nodes[prime])
                nodes[prime].neighbors.append(nodes[n])
        
        def dfs(node, seen):
            if node.val in seen:
                return 
            if node.val in filtered:
                filtered.remove(node.val)
            seen.add(node.val)
            for n in node.neighbors:
                dfs(n, seen)
        seen = set()
        key = next(iter(nodes))
        dfs(nodes[key], seen)
        return  len(filtered) == 0

            

