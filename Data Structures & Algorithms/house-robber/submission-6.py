class Solution:
    def rob(self, nums: List[int]) -> int:

        # def helper(i):
        #     if i==0:
        #         return nums[0]
        #     if i==1:
        #         return max(nums[0], nums[1])
        #     return max(nums[i]+helper(i-2), helper(i-1))
        
        # return helper(n-1)
        #topdown approach which neds dic and helper
        # n = len(nums)
        # if nums == 1:
        #     return nums[0]
        # if n == 2:
        #     return max(nums[0], nums[1])

        # memo = {0:nums[0], 1: max(nums[0], nums[1]) }  #stores max at each index
        # def helper(i):
        #     if i in memo:
        #         return memo[i]
        #     else:
        #         memo[i] = max(nums[i]+helper(i-2), helper(i-1))
        #         return memo[i]
        # return helper[n-1]
        #bottom up approach which just needs array
        n = len(nums)
        print(len(nums))
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[n-1]
        


        