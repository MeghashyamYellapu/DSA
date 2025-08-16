class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=float("inf")
        n=len(nums)
        temp=[]
        l=0
        for r in range(n):
            temp.append(nums[r])
            # if (r-l==k):
            #     l+=1
            if r-l+1==k:
                ans=min(ans,temp[r]-temp[l])
                l+=1
        return ans