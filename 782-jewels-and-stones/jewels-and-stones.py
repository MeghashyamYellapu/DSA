class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dici={}
        for i in jewels:
            dici[i]=0
        ans=0
        for j in dici:
            for i in range(len(stones)):
                if j==stones[i]:
                    ans+=1
        return ans