class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini=nums[0]
        maxi=0
        for i in range(len(nums)):
            mini = min(nums[i],mini)
            if nums[i]-mini>maxi:
                maxi=nums[i]-mini
        
        if(maxi==0):
            return -1
        else:
            return maxi
            
            