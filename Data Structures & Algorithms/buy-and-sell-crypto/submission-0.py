class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest1 = prices[0]
        highest1 = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            highest1 = max(highest1, prices[i])
            if prices[i] < lowest1:
                profit = max(profit, highest1 - lowest1)

                lowest1 = highest1 = prices[i]
        profit = max(profit, highest1 - lowest1)
        return profit


