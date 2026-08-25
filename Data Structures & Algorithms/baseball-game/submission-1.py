import math
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        

        newlist = []
        for i in range(len(operations)):
            if operations[i] == "+":
                newlist.append(int(newlist[-1])+int(newlist[-2]))
            elif operations[i] == "C":
                # newlist.remove(newlist[-1])
                newlist.pop()
            elif operations[i] == "D":
                newlist.append(int(newlist[-1])*2)
            else:
                newlist.append(operations[i])
        
        total = sum(int(x) for x in newlist)
        return total



