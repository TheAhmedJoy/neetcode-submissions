class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        leftover_students = len(students)
        student_type = Counter(students)

        for sandwich in sandwiches:
            if student_type[sandwich] > 0:
                leftover_students -= 1
                student_type[sandwich] -= 1
            else:
                break
        
        return leftover_students