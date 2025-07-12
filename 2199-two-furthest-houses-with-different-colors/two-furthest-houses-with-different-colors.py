class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=0
        for i in range (len(colors)):
            for j in range (i,len(colors)):
                if colors[i]!=colors[j]:
                    sum1 =j-i
                    if sum1>ans:
                        ans=sum1
        return ans
        