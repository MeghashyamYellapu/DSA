class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def count(arr,k):
            n=len(arr)
            ans=0
            l=0
            count=0
            for r in range(n):
                if arr[r]%2==1:
                    count+=1
                while count>k:
                    if arr[l]%2==1:
                        count-=1
                    l+=1
                ans+=r-l+1
            return ans
        return count(nums,k)-count(nums,k-1)