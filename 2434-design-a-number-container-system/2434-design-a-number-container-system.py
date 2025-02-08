class NumberContainers:

    def __init__(self):
        # heap?
        self.n_map = {} # n: heap, ignore
        self.i_map = {} # i: n
        

    def change(self, index: int, number: int) -> None:
        if index in self.i_map and self.i_map[index] == number:
            return

        if index in self.i_map:
            old_n = self.i_map[index]
            self.n_map[old_n][1].add(index)

        if number in self.n_map:
            self.n_map[number][1].discard(index)
        else:
            self.n_map[number] = ([], set())


        self.i_map[index] = number 
        heapq.heappush(self.n_map[number][0], index)

    def find(self, number: int) -> int:
        if number not in self.n_map:
            return -1
        
        heap, ignore = self.n_map[number]

        while heap and heap[0] in ignore:
            heapq.heappop(heap)
        
        self.n_map[number] = (heap, ignore)
        
        return heap[0] if heap else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)