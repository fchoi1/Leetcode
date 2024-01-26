class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(set)
        canTake = set()
        # Preprocess
        for a, b in prerequisites:
            courseMap[a].add(b)

        def checkCourse(course, seen):
            if course in canTake or not courseMap[course]:
                canTake.add(course)
                return False

            if course in seen:
                return True
            seen.add(course)

            for course in courseMap[course]:
                if checkCourse(course, seen):
                    return True
                canTake.add(course)
            return False

        for course in range(numCourses):
            if course in canTake:
                continue
            if checkCourse(course, set()):
                return False
        return True
        