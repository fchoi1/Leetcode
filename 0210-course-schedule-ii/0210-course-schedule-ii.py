class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        courseMap = defaultdict(set)
        taken = set()
        res = []

        for a,b in prerequisites:
            courseMap[a].add(b)

        print(courseMap)
        def checkCourse(course, seen, taken):
            if course in seen:
                return False
            if not courseMap[course]:
                if course not in taken:
                    taken.add(course)
                    res.append(course)
                return True
            
            seen.add(course)
            for c in courseMap[course]:
                if c in taken:
                    continue
                if not checkCourse(c, seen, taken):
                    return False
            seen.remove(course)
            if course not in taken:
                res.append(course)
                taken.add(course)
            return True

        # if loops end it
        for i in range(numCourses):
            if i in taken:
                continue
            if not checkCourse(i, set(), taken):
                return []
        return res