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
        print("target", t)
        while  l < r:
            mid = math.ceil((l + r ) / 2)
            print(l,r, mid,self.time_list[mid][0] )
            if t == self.time_list[mid][0]:
                return self.time_list[mid][1]
            elif t > self.time_list[mid][0]:
                l = mid 
            else:
                r = mid - 1
            print("AFTER",l, r, mid)
        return self.time_list[l][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)