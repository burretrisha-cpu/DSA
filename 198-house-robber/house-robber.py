class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        p2,p1=0,0
        for i in nums:
            x=max(p1,p2+i)
            p2=p1
            p1=x
        return p1
        