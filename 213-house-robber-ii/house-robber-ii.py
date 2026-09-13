class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def r(s):
            p2,p1=0,0
            for i in s:
                x=max(p1,p2+i)
                p2=p1
                p1=x
            return p1
        return max(
            r(nums[:-1]),
            r(nums[1:])
        )
            