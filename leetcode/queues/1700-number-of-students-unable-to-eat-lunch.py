from typing import List


# first solution
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches.reverse()

        while len(sandwiches) > 0 and students.count(sandwiches[-1]) > 0:
            if students[0] == sandwiches[-1]:
                students.pop(0)
                sandwiches.pop()
            else:
                removedStudent = students.pop(0)
                students.append(removedStudent)

        return len(students)


# second solution with O(n) time complexity
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        numStudentsPerSandwich = {0: 0, 1: 0}
        for student in students:
            numStudentsPerSandwich[student] += 1

        for sandwich in sandwiches:
            if numStudentsPerSandwich[sandwich] > 0:
                numStudentsPerSandwich[sandwich] -= 1
            else:
                break

        numStudentsUnable = numStudentsPerSandwich[0] + numStudentsPerSandwich[1]
        return numStudentsUnable
