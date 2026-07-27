class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength=0
        left=0
        window=0
        c=set()
        for right in range(len(s)):
            while s[right] in c:
                c.remove(s[left])
                left+=1
            c.add(s[right])
            maxlength=max(maxlength,right-left+1)
        return maxlength