class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        temp=0
        l=0
        for r in range(n):
            if nums[r]==0:
                temp+=1
            while temp>1:
                if nums[l]==0:
                    temp-=1
                l+=1
            ans=max(ans,r-l)
        return ans