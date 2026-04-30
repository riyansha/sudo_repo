class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = {len(nums)-1: 1}
        def sublong(idx):
            #STORES INDEX AS KEY AND CORRESPONDING AND FROM THAT INDEX THE LENGTH OF LONEST INCREASING SUBSEQUNEC
               #only the element itself
            longest = 1  # the value itself
            if idx in LIS:
                return LIS[idx]
            for j in range(idx+1, len(nums)):   #starts backward
                if nums[j] > nums[idx]:
                    longest = max(longest, 1 + sublong(j))   #simply return longest length from that point to be 1 sinc elast element cant be included
            LIS[idx] = longest
            return longest
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, sublong(i))
        
        return ans
      

        