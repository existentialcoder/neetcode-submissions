class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            buy_price = prices[l]
            sell_price = prices[r]

            if buy_price < sell_price:
                profit = max(profit, sell_price - buy_price)
            else:
                l = r
            r += 1

        return profit