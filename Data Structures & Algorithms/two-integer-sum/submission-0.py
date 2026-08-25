class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap_dict = {}

        for key, value in enumerate(nums):
            remain = target - value
            if remain in hashMap_dict:
                return [hashMap_dict[remain], key]
            hashMap_dict[value] = key


        