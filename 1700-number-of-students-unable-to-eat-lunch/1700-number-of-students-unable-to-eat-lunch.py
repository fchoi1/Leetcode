class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # 0 1
        # 0 1
        ones = students.count(1)
        zeros = students.count(0)
        while ones > 0 and zeros > 0 and sandwiches and students:
            print("here",ones, zeros, students, sandwiches)
            while students and sandwiches and students[0] == sandwiches[0]:
                if students[0]:
                    ones -= 1
                else:
                    zeros -= 1
                sandwiches.pop(0)
                students.pop(0)
            if not sandwiches or not students:
                break
            students.append(students.pop(0))
        print("done", ones , zeros , sandwiches)
        return len(sandwiches)
        # 1  1 1 0 0 1
        # 1  0 0 0 1 1

        # 1 1 1
        # 0 1 1

        # 0 0 0 0
        # 1 0 0 0
        