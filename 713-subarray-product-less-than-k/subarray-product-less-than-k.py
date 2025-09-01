class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=0:
            return 0
        def atmost(nums,k):
            n=len(nums)
            ans=0
            temp=1
            l=0
            for r in range(n):
                temp*=nums[r]
                while temp>=k and l<=r :
                    temp/=nums[l]
                    l+=1
                ans+=r-l+1
            return ans
        return atmost(nums,k)

                