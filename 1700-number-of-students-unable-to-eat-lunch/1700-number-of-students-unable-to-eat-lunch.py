class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)

        for s in sandwiches:
            if counts[s] != 0:
                counts[s] -= 1
            else:
                return sum(counts.values())
        return 0