class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        target = total - x
        n = len(nums)

        # Edge case: if target < 0, it's impossible
        if target < 0:
            return -1
        # Edge case: if target == 0, remove all elements
        if target == 0:
            return n

        ans = -1
        curr_sum = 0
        l = 0

        for r in range(n):
            curr_sum += nums[r]

            # shrink window if sum exceeds target
            while curr_sum > target and l <= r:
                curr_sum -= nums[l]
                l += 1

            # check if valid window
            if curr_sum == target:
                ans = max(ans, r - l + 1)

        return -1 if ans == -1 else n - ans