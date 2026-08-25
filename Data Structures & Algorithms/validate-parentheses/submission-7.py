class Solution:
    def isValid(self, s: str) -> bool:
        # {}()[]
        # same open and close bracket, ([{}])
        # have corrosponding bracket
        # list1 = []
        # for i in s:
        #     if i == "(" or i =="[" or i == "{":
        #         list1.append(i)
        #     if list1 == [] and (i== ")" or i =="}" or i == "]"):
        #         return False
        #     if (i == "}" and list1[-1] == "{") or (i == "]" and list1[-1] == "[") or (i == ")" and list1[-1] == "("):
        #         list1.pop()
            
        #     print(list1)

        # print(list1)   
        # if list1 == []:
        #     return True
        # else:
        #     return False 


        dict1 = {"{":"}","[":"]","(":")"}
        list1 = []
        boo = True

        for i in s:
            for k,v in dict1.items():
                if i == k:
                    list1.append(i)
                if i == v:
                    if list1 != []:
                        if list1[-1] == k:
                            list1.pop()
                            continue
                        else:
                            return False
                    if list1 == []:
                        
                        return False
                        break
                        
               
            
        if list1 == [] :
            return True
        else:
            return False 
                

            