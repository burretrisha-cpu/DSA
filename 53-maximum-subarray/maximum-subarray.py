class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxS=nums[0]
        cur_sum=0
        for i in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum+=i
            maxS=max(maxS,cur_sum)
        return maxS
        