class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l=0
        n=len(answerKey)
        countf=0
        countt=0
        ans=0
        for r in range(n):
            if answerKey[r]=='F':
                countf+=1
            else:
                countt+=1
            while min(countf,countt)>k:
                if answerKey[l]=='F':
                    countf-=1
                else:
                    countt-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans

        