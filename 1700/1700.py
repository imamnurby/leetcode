class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    
        while sandwiches:

            if sandwiches[0] == students[0]:
                students = students[1:]
                sandwiches = sandwiches[1:]
            else:
                students.append(students[0])
                students = students[1:]

            if sandwiches and sandwiches[0] not in students:
                break

        return len(students)
        
