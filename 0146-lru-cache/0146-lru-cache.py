class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.nodes = {} # Doubly Linked List
        self.end = None # end node
        self.start = None # start node
        self.capacity = capacity
        
    def updateKey(self, key):
        if self.end != key:
            prev_node, next_node = self.nodes[key]

            if self.start == key:
                self.start = next_node
            
            # Remove key from curr position
            self.nodes[next_node] = (prev_node, self.nodes[next_node][1])
            if prev_node != None:
                self.nodes[prev_node] = (self.nodes[prev_node][0], next_node)
            
            # Add key to end
            self.nodes[key] = (self.end, None)
            self.nodes[self.end] = (self.nodes[self.end][0], key)

            self.end = key

    def get(self, key: int) -> int:
        if key in self.cache:
            self.updateKey(key)
            return self.cache[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        # Add new key to end of linked list
        if key not in self.cache: 
            if self.start == None:
                self.start = key
            else:
                self.nodes[self.end] = (self.nodes[self.end][0], key)
            self.nodes[key] = (self.end, None)
            self.end = key
        # update existing key to end
        else:
            self.updateKey(key)
                    
        self.cache[key] = value
        
        # remove start key if over limit
        if len(self.cache) > self.capacity:
            new_start = self.nodes[self.start][1]
            del self.nodes[self.start]
            del self.cache[self.start]
            self.nodes[new_start] = (None, self.nodes[new_start][1])
            self.start = new_start
