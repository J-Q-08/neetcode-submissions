class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, maxcash = 0, 1, 0
        
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maxcash = max(maxcash, prices[r] - prices[l])
                r += 1
        return maxcash