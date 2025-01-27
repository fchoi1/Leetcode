class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        # map to store all prereqs

        self.adjMap = defaultdict(set)
        self.in_nodes = defaultdict(set)
        self.courses = {}

        for a,b in prerequisites:
            self.adjMap[a].add(b)
            self.in_nodes[b].add(a)

        def getList(node):
            if node not in self.in_nodes:
                self.courses[node] = set()
                return set()
            
            if node in self.courses:
                return self.courses[node]

            dep = set()
            for in_node in self.in_nodes[node]:
                dep.add(in_node)
                dep |= getList(in_node)

            self.courses[node] = dep
            return dep

        for i in range(numCourses):
            # only Sinks
            if i not in self.adjMap:
                getList(i)

        return [u in self.courses[v] for u,v in queries]