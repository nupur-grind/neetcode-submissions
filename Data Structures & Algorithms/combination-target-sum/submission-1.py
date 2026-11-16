class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # dfs with i, curr, total
        # res has the copy of curr
        # call dfs with 0 and [] empty
        # base case: if total = target, return, if i >=len or total > taget, reutrn 
        # add to curr with num[i] 
        # call dfs with i , curr, total + nums
        # remove from curr 
        # call dfs with i+1 , curr, total . bc total will remain but we have to find the next number so i+1

        res = []

        def dfs(i, curr, total):

            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            curr.pop()
            dfs(i+1, curr, total)

        
        dfs(0,[],0)
        return res





