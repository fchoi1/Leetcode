class Node:
    def __init__(self, val ,parent=None):
        self.val = val
        self.children = {}
        self.parent = parent
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        h = len(board)
        w = len(board[0])

        root = Node(None)
        res = []
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    newNode = Node(char, node)
                    node.children[char] = newNode
                else:
                    newNode = node.children[char]
                node = newNode
            node.isEnd = True

        def inRange(x, y):
            return 0 <= x < w and 0 <= y < h

        def dfs(node, word, coord, visited):
            if coord in visited:
                return
            visited.add(coord)            
            x,y = coord
            char = board[y][x]
            
            if char not in node.children:
                visited.remove(coord) 
                return

            newNode = node.children[char]
            if newNode.isEnd:
                res.append(word + char)
                newNode.isEnd = False
                if len(newNode.children) == 0:
                    for c in (word+char)[::-1]:
                        if not node:
                            break
                        if len(node.children) == 1:
                            node.children = {}
                            node = node.parent
                        else:
                            del node.children[c]
                            break
           
            for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                newX, newY = x + dx, y + dy
                if inRange(newX, newY) and (newX, newY) not in visited:
                    dfs(newNode, word + char, (newX, newY), visited)
            visited.remove(coord) 

        
        for y in range(h):
            for x in range(w):
                char = board[y][x]
                if char in root.children:
                    dfs(root, '',(x,y), set())
        return res