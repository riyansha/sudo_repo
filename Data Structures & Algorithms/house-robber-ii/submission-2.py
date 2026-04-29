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
      
        # def rob_linear(arr):
        #     prev2 = 0  # dp[i-2]
        #     prev1 = 0  # dp[i-1]
            
        #     for x in arr:
        #         curr = max(prev1, prev2 + x)
        #         prev2 = prev1
        #         prev1 = curr
            
        #     return prev1

        # n = len(nums)
        
        # if n == 1:
        #     return nums[0]
        
        # return max(
        #     rob_linear(nums[:-1]),  # exclude last
        #     rob_linear(nums[1:])    # exclude first
       
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def helper(arr):
            memo = {0: arr[0], 1: max(arr[0], arr[1])}
            
            def dp(i):
                if i in memo:
                    return memo[i]
                memo[i] = max(arr[i] + dp(i-2), dp(i-1))
                return memo[i]
            
            return dp(len(arr)-1)

        # 🔥 only change: split into two cases
        return max(helper(nums[:-1]), helper(nums[1:]))
        
        # for i in range(2, n):
        #     dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        # return dp[n-1]
        


        