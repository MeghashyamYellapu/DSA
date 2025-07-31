class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        print(dici)
        ans=0
        for val1 in dici:
            val=dici[val1]
            if val>1:
                ans += val * (val - 1) // 2

            
        return ans

