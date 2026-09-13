class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        def mcs(i):
            if i>=len(cost):
                return 0
            if i in memo:
                return memo[i]
            memo[i]=cost[i]+min(
                mcs(i+1),
                mcs(i+2)
            )
            return memo[i]
        return min(mcs(0),mcs(1))


        