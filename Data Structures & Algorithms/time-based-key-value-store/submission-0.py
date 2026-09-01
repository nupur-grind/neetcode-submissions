
class TimeMap:
    # for set if we do map[k] = val, then it will throw duplicate error and if we do that for existing key, it will overwrite. So we have to create key list if key not there and else, append the val to the key
    # Binary search because timestamp is always increasing and so sorted arr, and we need T: O(logn) statisfied.
    # get(): l,r. target uses .get(k,[]), to get key, if not there then take [].
    # sso val will be m = (l+r)//2 and timestamp will be -1

    def __init__(self):
        self.hashMap = {} #key ,[value,timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append([value,timestamp])
        # self.hashMap[key] = [value,timestamp]
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        target = self.hashMap.get(key,[])
        l=0
        r = len(target)-1

        while l <= r:
            m = (l+r)//2

            # how is this m[1] and why is res = m [0] ?? shouldn't it be m [-1] <= timestamp ?
            if target[m][1] <= timestamp: 
                res = target[m][0]
                l= m+1
            else:
                r = m-1
        return res

    
            
        
#  key = [(bar,1), (bar,2), (bar,3), (gril,1), (gril,2)]