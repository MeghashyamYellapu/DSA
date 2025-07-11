class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
    
        for i in range (1,len(s)):
            sum2= ord(s[i-1])-ord(s[i])
            if(0>sum2):
                sum2=sum2*-1
            sum+=sum2
               
        return sum