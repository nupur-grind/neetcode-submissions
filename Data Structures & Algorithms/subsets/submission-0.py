class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res is where the subset sends final copy
        # subset is what has the curr sets
        # backtracking dfs mostly 
        # dfs, if i is >=len , return 
        # call dfs as 0 as 0th index
        # first add to subset the num and increase i
        # remove from subset and increase i

        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return res