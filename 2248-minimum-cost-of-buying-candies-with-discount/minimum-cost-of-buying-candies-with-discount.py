class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        took=0
        ans=0
        n= len(cost)
        for r in range(n-1,-1,-1):
            if took==2:
                took=0
            else:
                ans+=cost[r]
                took+=1
        return ans