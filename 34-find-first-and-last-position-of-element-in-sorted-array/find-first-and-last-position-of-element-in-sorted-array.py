class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        if len(nums)==1 and target==nums[0]:
            return [0,0]
        def left (nums,target):
            l=0
            r=len(nums)-1
            while(l<=r):
                mid=int(l+(r-l)/2)
                
                if nums[mid]>=target:
                    r=mid-1
                else :
                    l=mid+1
            print(l)
            if (l<0 or l>=len(nums))  or nums[l]!=target :
                return -1
            elif nums[l]==target:
                return l
            else :
                return -1
        def right (nums,target):
            l=0
            r=len(nums)-1
            while(l<=r):
                mid=int(l+(r-l)/2)
                if nums[mid]>target:
                    r=mid-1
                else :
                    l=mid+1
                print(ans,mid)
            
            if (r<0 or r>=len(nums))  or nums[r]!=target :
                return -1
            elif nums[r]==target:
                return r
            else :
                return -1
        
        ans[1]=right(nums,target)
        ans[0]=left(nums,target)
        # if ans[0]=='':
        #     ans[0]=ans[1]
        # ans.sort()
          
        return ans