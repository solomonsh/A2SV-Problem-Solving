class Solution:
    def countStudents(self, students, sandwiches):
        
        while students:
            
            if sandwiches[0] not in students:
                break
            
            if students[0] == sandwiches[0]:
                
                students.pop(0)
                sandwiches.pop(0)
                
            else:
                students.append(students.pop(0))
        
        return len(students)
        