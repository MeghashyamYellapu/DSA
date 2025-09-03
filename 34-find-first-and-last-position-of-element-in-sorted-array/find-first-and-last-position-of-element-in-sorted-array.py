class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        def right(nums,target):
            l=0
            r=len(nums)-1
            while(l<=r):
                mid=int(l+(r-l)/2)
                if nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            if (r<0 or r>=len(nums)) or nums[r]!=target:
                return -1
            return r
        def left(nums,target):
            l=0
            r=len(nums)-1
            while(l<=r):
                mid=int(l+(r-l)/2)
                if nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            if (l<0 or l>=len(nums)) or nums[l]!=target:
                return -1
            return l
        ans[0]=left(nums,target)
        ans[1]=right(nums,target)
        print(ans)
        return ans