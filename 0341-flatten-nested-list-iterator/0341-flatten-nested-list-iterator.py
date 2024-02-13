class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        nested = nestedList
        stack = []
        self.index = 0
        self.flatten = []
        i = 0
        while stack or i < len(nested):
            while stack and i >= len(nested):
                nested, i = stack.pop()
            
            if nested[i].isInteger():
                val = nested[i].getInteger()
                self.flatten.append(val)
                i += 1
                continue
                
            if i + 1 < len(nested):
                stack.append((nested, i+1))
            nested = nested[i].getList()
            i = 0
    
    def next(self) -> int:
        self.index += 1
        return self.flatten[self.index - 1]
       
    
    def hasNext(self) -> bool:
        return self.index < len(self.flatten)
         