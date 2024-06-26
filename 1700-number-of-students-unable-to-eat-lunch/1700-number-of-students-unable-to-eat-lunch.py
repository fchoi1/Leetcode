class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_students = Counter(students)
        
        while sandwiches and count_students[0] > 0 and count_students[1] > 0:
            count_students[sandwiches.pop(0)] -= 1

        val = 0 if count_students[0] > 0 else 1

        while sandwiches and sandwiches[0] == val:
            sandwiches.pop(0)
        return len(sandwiches)