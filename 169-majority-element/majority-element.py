class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dici={}
        for i in range(len(nums)):
            temp=1
            if nums[i] in dici:
                dici[nums[i]]=dici[nums[i]]+1
            else:
                dici[nums[i]]=temp
        print(dici)
       
        for i in dici:
            if dici[i] >len(nums)/2:

                print(i)
                return i
            # else:
            #     i=i+1