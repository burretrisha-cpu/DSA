class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st = {}
        ts = {}
        for i in range(len(s)):
            c1=s[i]
            c2=t[i]
            if c1 in st:
                if st[c1]!=c2:
                    return False
            else:
                st[c1]=c2
            if c2 in ts:
                if ts[c2]!=c1:
                    return False
            else:
                ts[c2]=c1
        return True
                    




        