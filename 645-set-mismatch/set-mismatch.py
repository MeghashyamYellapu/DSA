class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        li = []
        s = set(nums)
        
        # Find duplicate
        for i in range(1, len(nums) + 1):
            if nums.count(i) == 2:  # count per number
                li.append(i)
                break
        
        # Find missing
        for i in range(1, len(nums) + 1):
            if i not in s:
                li.append(i)
                break
        
        return li