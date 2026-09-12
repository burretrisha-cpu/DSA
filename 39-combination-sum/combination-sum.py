class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def solve(i,ans,sum):
            if sum==target:
                res.append(ans[:])
                return
            if sum>target:
                return
            for j in range(i,len(candidates)):
                ans.append(candidates[j])
                solve(j,ans,sum+candidates[j])
                ans.pop()
        solve(0,[],0)
        return res
                

        