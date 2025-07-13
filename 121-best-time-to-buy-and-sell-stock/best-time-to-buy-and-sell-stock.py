class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        mini=prices[0]
        for i in range (0,len(prices)):
            mini=min(mini,prices[i])
            sum1 = prices[i]-mini
            if sum1>ans :
                ans=sum1
        return ans
                
        