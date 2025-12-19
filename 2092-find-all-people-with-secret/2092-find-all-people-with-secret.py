class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # combine all the linkages, particular order
        # sort by time,

        secret = set()

        # bfs
        h = [(0,0), (0, firstPerson)] # time, person

        adjMap = defaultdict(dict)
        for x,y,time in meetings:

            if y not in adjMap[x]:
                adjMap[y][x] = []
                adjMap[x][y] = []
      
            adjMap[x][y].append(time)
            adjMap[y][x].append(time)



        while h:    # queue of people w/ secret
            time, person = heapq.heappop(h)
            if person in secret:
                continue
            secret.add(person)
    

            for nextPerson, meetingTimes in adjMap[person].items():
                for meetingTime in meetingTimes:
                    if meetingTime < time:
                        continue
                    heapq.heappush(h, (meetingTime, nextPerson))


        return list(secret)


