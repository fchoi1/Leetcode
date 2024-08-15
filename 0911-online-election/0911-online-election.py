class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        sorted_times = sorted((t,p) for t,p in zip(times, persons))
        people = defaultdict(int)
        leader = (0, None)
        self.time_list = []

        for t,p in sorted_times:
            people[p] += 1
            if people[p] >= leader[0]:
                leader = (people[p], p)
            self.time_list.append((t, leader[1]))
        
        print(self.time_list)

    def q(self, t: int) -> int:
        l = 0
        r = len(self.time_list) - 1
        while  l < r:
            mid = math.ceil((l + r ) / 2)
            if t == self.time_list[mid][0]:
                return self.time_list[mid][1]
            elif t > self.time_list[mid][0]:
                l = mid 
            else:
                r = mid - 1
        return self.time_list[l][1]

