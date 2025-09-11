import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        r=max(nums)
        d=0
        l=1
        ans=0
        while(l<=r):
            d=int((l+r)/2)
            total=0
            for i in range(n):
                total+=math.ceil(nums[i]/d)
            print(total)
            if total>threshold:
                l=d+1
            else:
                ans=d
                r=d-1
        return ans