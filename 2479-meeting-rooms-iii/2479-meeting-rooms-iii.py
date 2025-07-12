class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = defaultdict(int)
        max_room = 0
        max_room_num = 0
        meetings.sort()

        # curr meetings
        h = [] # end time, room

        avail = [i for i in range(n)]
        heapify(avail)
        print("AV", avail)
        # track avail meetings?
        for s,e in meetings:

            while h and s >= h[0][0]:
                _, free = heappop(h)
                heappush(avail, free)

            if avail:
                free = heappop(avail)
                heappush(h, (e, free))
            else:
                # no available rooms? backlog? 
                # update meeting to to earliest end?
                end, free = heappop(h)
                heappush(h, (end + (e - s), free))

            rooms[free] += 1
            if rooms[free] > max_room:
                max_room = rooms[free]
                max_room_num = free
            elif rooms[free] == max_room:
                max_room_num = min(max_room_num, free)
        # print(rooms, max_room_num, "count", max_room)
        return max_room_num


        