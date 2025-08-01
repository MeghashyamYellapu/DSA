class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dici={}
        ch='a'
        ans=""
        for i in key:
            if i not in dici and i !=' ' :
                dici[i]=ch
                ch=chr(ord(ch)+1)
        for i in message:
            if i !=' ':
                ans+=dici[i]
            else:
                ans+=' '
            
        return ans
                