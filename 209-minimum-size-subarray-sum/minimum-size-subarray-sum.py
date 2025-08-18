class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=float("inf")
        temp=0
        l=0
        n=len(nums)
        for r in range(n):
            temp+=nums[r]
            while temp>=target:
                ans=min(ans,r-l+1)
                temp-=nums[l]
                l+=1
        return 0 if ans==float("inf") else ans