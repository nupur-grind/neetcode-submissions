class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
       
        count = 0
        i = 0
        j = 0

        # for i in students:
        #     for j in sandwiches:
        #         if students[0] == sandwiches[0]:
        #             students.pop(0)
        #             sandwiches.pop(0)
        #             print("IF students: ",students, " sandwiches: ", sandwiches)
        #         else:
        #             students.append(students.pop(0))
        #             print("ELSE students: ",students, " sandwiches: ", sandwiches)
        #         if students == sandwiches:
        #             sandwiches.clear()
        #             students.clear()
        #         i+=1
        #         j+=1

        while students:
            if not students:
                break;
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                print("IF students: ",students, " sandwiches: ", sandwiches)
            else:
                students.append(students.pop(0))
                if sandwiches[0] not in students:
                    break
                print("ELSE students: ",students, " sandwiches: ", sandwiches)
            if students == sandwiches:
                sandwiches.clear()
                students.clear()

        print(students)
        count = len(students)
        return count

        
        