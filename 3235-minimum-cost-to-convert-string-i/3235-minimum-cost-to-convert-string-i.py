class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:


        def fill_cost(start):
            q = [(0, start)]
            letter_cost = {}
            while q:
                curr_cost, letter= heapq.heappop(q)

                if letter in letter_cost:
                    continue
                letter_cost[letter] = curr_cost

                for next_letter in adj_list[letter]:
                    heapq.heappush(q, (curr_cost + adj_list[letter][next_letter], next_letter))
                    
            return letter_cost

        cost_dict = {}
        adj_list = defaultdict(dict)

        for s,e,c in zip(original, changed, cost):
            adj_list[s][e] = min(adj_list[s].get(e,inf),c)

        for letter in "abcdefghijklmnopqrstuvwxyz":
            cost_dict[letter] = fill_cost(letter)

        min_cost = 0
        for start,end in zip(source, target):
            if end not in cost_dict[start]:
                return -1
            min_cost += cost_dict[start][end]
        return min_cost
        

        