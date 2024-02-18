class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        rooms = list(range(n))
        roomCount = [0] * n
        ongoing = []
        maxCount = roomNum = 0
        for start, end in meetings:
            while ongoing and start >= ongoing[0][0]:
                _, num = heapq.heappop(ongoing)
                heapq.heappush(rooms,num)

            if len(rooms) != 0:
                avail = heapq.heappop(rooms)
                heapq.heappush(ongoing,(end, avail))
            else:
                prevEnd, avail = heapq.heappop(ongoing)
                heapq.heappush(ongoing,(prevEnd + end - start, avail))

            roomCount[avail] += 1
            if roomCount[avail] > maxCount:
                maxCount, roomNum = roomCount[avail],avail
            elif roomCount[avail] == maxCount:
                roomNum = min(roomNum, avail)
        return roomNum
        