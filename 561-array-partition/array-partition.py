class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        temp=[]
        ans=0
        l=0
        print(nums)
        for r in range(0, n, 2):
            ans+=min(nums[r],nums[r+1])
            
            print(ans)

        return ans

