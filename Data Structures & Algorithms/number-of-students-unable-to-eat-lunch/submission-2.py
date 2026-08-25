class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
       
        count = 0
        i = 0
        j = 0

        while students:
            if not students:
                break;
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
                if sandwiches[0] not in students:
                    break
            if students == sandwiches:
                sandwiches.clear()
                students.clear()

        count = len(students)
        return count

        
        