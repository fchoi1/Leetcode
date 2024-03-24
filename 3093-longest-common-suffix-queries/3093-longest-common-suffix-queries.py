class Node:
    def __init__(self, char, length, index):
        self.char = char
        self.index = index
        self.length = length
        self.next = {}
        self.end = False

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        res = []
        
        node = root = Node('',inf,-1)
        # build tree
        for i,word in enumerate(wordsContainer):
            node = root
            if len(word) < root.length:
                root.length = len(word)
                root.index = i
            for s in word[::-1]:
                if s not in node.next:
                    newNode = Node(s, len(word),i)
                    node.next[s] = newNode
                else:
                    if len(word) < node.next[s].length:
                        node.next[s].length = len(word)
                        node.next[s].index = i
                node = node.next[s]

            
        node = root
        # print(root.next['d'].index)
                
        for word in wordsQuery:
            node = root
            for s in word[::-1]:
                if s in node.next:
                    node = node.next[s]
                else:
                    break
            
            res.append(node.index)
        return res
                    
                
                