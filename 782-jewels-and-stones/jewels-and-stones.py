class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dici={}
        for i in jewels:
            dici[i]=0
            print(dici)
        ans=0
        for i in range(len(stones)):
            # print(stones[i],dici[stones[i]])
            if stones[i] in dici:
                dici[stones[i]]+=1
                ans+=1
            print(dici)

        return ans