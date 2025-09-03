class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        l, r = 0, n - 1
        first_pos = n
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > 0:
                first_pos = mid
                r = mid - 1
            else:
                l = mid + 1

        # Binary search for last negative index
        l, r = 0, n - 1
        last_neg = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < 0:
                last_neg = mid
                l = mid + 1
            else:
                r = mid - 1

        count_pos = n - first_pos
        count_neg = last_neg + 1

        return max(count_pos, count_neg)
            