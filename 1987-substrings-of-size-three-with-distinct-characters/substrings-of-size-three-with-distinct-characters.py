class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l=0
        n=len(s)
        temp=[]
        ans=0
        for r in range(n):
            temp+=s[r]
            if r-l==3:
                temp.remove(s[l])
                l+=1
            if r-l+1==3:
                if temp[0]!=temp[1]:
                    if temp[1]!=temp[2]:
                        if temp[2]!=temp[0]:
                            ans+=1
        return ans
        