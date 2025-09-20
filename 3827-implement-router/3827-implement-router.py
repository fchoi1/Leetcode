class Router:

    def __init__(self, memoryLimit: int):
        # cache 
        # FIFO queue
        self.packet = set() # tuple (source, dest, timestamp)
        self.dest = defaultdict(deque) # dest: [timestamp] # sorted
        self.queue = deque()
        self.limit = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        # timestamp is already increasing
        key = (source, destination, timestamp) 
        if key in self.packet:
            return False
        
        if len(self.queue) == self.limit:
            self.forwardPacket()

        self.packet.add(key)
        self.dest[destination].append(timestamp)
        self.queue.append(key)
        return True
        

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        popped = self.queue.popleft()
        self.packet.remove(popped)
        self.dest[popped[1]].popleft()
        return popped
        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        dest_list = self.dest[destination]
        return bisect.bisect_right(dest_list,endTime)-bisect.bisect_left(dest_list,startTime)

        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)