# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         def change(target, coins):
#             breakup = {0:0, 1:1}
#             if target == 0:
#                 return 
#             #breakup stores no of "min" coins to get that amount for 0 its 0 for 1 its 1 (just a 1 rupee coin)
#             if target in breakup:
#                 return breakup[target].value
#             for i in range(len(coins)):
#                 if target > coins[i]:
#                     k_val = target - coins[i]
#                     breakup.append[target] = min(len(target - coins[]), len(target - coins[i]), len(target - coins[i]) )
#             return breakup[left].value
#         return change(amount, coins)
        


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        breakup = {}  # memoization
        def change(target):
            if target == 0:
                return 0
            if target < 0:
                return float('inf')
            if target in breakup:
                return breakup[target]
            min_coins = float('inf')
            for i in range(len(coins)):
                # res = change(target - coins[i])
                # if res != float('inf'):
                min_coins = min(min_coins, 1 + change(target - coins[i]))
            breakup[target] = min_coins
            return min_coins
        ans = change(amount)
        return -1 if ans == float('inf') else ans