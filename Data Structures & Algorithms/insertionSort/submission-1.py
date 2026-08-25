# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # 3, 4 , 1 , 2

        # for i in range(len(pairs)):
        #     j = i-1
        #     while j >=0 and i > (i+1):
        #         temp = i
        #         i = i+1
        #         i+1 = temp
        #         j-=1
        n = len(pairs)
        result = []
        for i in range(n):
            j = i-1
            while j>=0 and pairs[j].key > pairs[j+1].key:
                temp = pairs[j]
                pairs[j] = pairs[j+1]
                pairs[j+1] = temp
                # pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j-=1

            result.append(pairs[:])
        return result

