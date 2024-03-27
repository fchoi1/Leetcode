class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        courseMap = defaultdict(set)
        taken = set()
        res = []

        for a,b in prerequisites:
            courseMap[a].add(b)

        def checkCourse(course, seen, taken):
            if i in taken:
                return True
            if course in seen:
                return False

            seen.add(course)
            for c in courseMap[course]:
                if not checkCourse(c, seen, taken):
                    return False
            seen.remove(course)
            if course not in taken:
                res.append(course)
                taken.add(course)
            return True

        for i in range(numCourses):
            if i in taken:
                continue
            if not checkCourse(i, set(), taken):
                return []
        return res