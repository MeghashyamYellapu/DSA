class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans=0
        n=len(arr)
        temp=0
        l=0

        for r in range(n):
            temp+=arr[r]
            if r-l==k:
                temp-=arr[l]
                l+=1
            if r-l+1==k:
                if temp/k>=threshold:
                    ans+=1
        return ans

        