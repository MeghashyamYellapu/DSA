class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans=0
        for i in range(0,len(nums)):
            for j in  range(1,len(nums)):
                if nums[i]==nums[j] and i <j:
                    print(nums[i],nums[j])
                    ans+=1
        return ans
        


