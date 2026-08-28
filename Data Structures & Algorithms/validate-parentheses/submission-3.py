class Solution:
    def isValid(self, s: str) -> bool:
        # {}()[]
        # same open and close bracket, ([{}])
        # have corrosponding bracket
        list1 = []
        for i in s:
            if i == "(" or i =="[" or i == "{":
                list1.append(i)
            if list1[0] == ")" or list1[0] =="}" or list1[0] == "]":
                return False
            if i == "}" and list1[-1] == "{":
                list1.pop()
            if i == "]" and list1[-1] == "[":
                list1.pop()
            if i == ")" and list1[-1] == "(":
                list1.pop() 
            print(list1)

        print(list1)   
        if list1 == []:
            return True
        else:
            return False 


            

        