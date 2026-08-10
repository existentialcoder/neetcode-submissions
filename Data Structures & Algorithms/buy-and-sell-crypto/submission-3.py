class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r <= len(prices) - 1:
            computed_buy_price = prices[l]
            computed_sell_price = prices[r]

            if computed_buy_price < computed_sell_price:
                computed_profit = computed_sell_price - computed_buy_price
                profit = max(profit, computed_profit)

            else:
                l = r
            r += 1

            

        return profit