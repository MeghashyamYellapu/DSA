class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        ans=0
        l=0
        dici={}

        for r in range(n):
            temp=fruits[r]
            if temp not in dici:
                dici[temp]=1
            else:
                dici[temp]+=1

            while len(dici)>2:
                lval=fruits[l]
                dici[lval]-=1
                if dici[lval]==0:
                    dici.pop(lval)
                l+=1
            ans=max(ans,r-l+1)
        return ans
            
        

           
            

            