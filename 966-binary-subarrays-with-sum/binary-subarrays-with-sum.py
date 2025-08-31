class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def sum1(arr,k):
            n=len(arr)
            ans=0
            temp=0
            l=0
            for r in range(n):
                temp+=arr[r]
                while temp>k:
                    temp-=arr[l]
                    l+=1
                ans+=r-l+1
            return ans
        if goal>0:
            return sum1(nums,goal)-sum1(nums,goal-1)
        else:
            return sum1(nums,goal)