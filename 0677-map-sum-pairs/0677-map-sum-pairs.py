class Node:
    def __init__(self):
        self.val = 0
        self.neigbors = {}

class MapSum:

    def __init__(self):
        self.root = Node()
        self.map = {}
        
    def insert(self, key: str, val: int) -> None:
        subtract = self.map[key] if key in self.map else 0
        self.map[key] = val
        
        node = self.root
        for char in key:
            if char not in node.neigbors:
                node.neigbors[char] = Node()
            node = node.neigbors[char]
            node.val += val - subtract

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.neigbors:
                return 0
            node = node.neigbors[char]
        return node.val
