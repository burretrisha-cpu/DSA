class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def solve(ans):
            if len(ans)==len(nums):
                res.append(ans[:])
                return
            for i in nums:
                if i in ans:
                    continue
                ans.append(i)
                solve(ans)
                ans.pop()
        solve([])
        return res
                
        