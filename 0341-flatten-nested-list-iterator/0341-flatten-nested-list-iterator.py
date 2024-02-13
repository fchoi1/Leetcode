# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # flatten here?
        self.index = 0
        self.nested = nestedList
        stack = []
        self.flatten = []
        i = 0
        while stack or i < len(self.nested):
            while stack and i >= len(self.nested):
                self.nested, i = stack.pop()
            # if not self.stack and i >= len(self.nested):
            #     break
            
            if self.nested[i].isInteger():
                val = self.nested[i].getInteger()
                self.flatten.append(val)
                i += 1
                continue
                
            if i + 1 < len(self.nested):
                stack.append((self.nested, i+1))
            self.nested = self.nested[i].getList()
            i = 0
    
    def next(self) -> int:
        self.index += 1
        return self.flatten[self.index - 1]
       
    
    def hasNext(self) -> bool:
        return self.index < len(self.flatten)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())