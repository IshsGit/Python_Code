class Solution:
    def maxProfit(prices):
        # idx as key
        days = {}
        value = 0
        for idx, price_i in enumerate(prices):
            print("price_i in days", price_i in days)

            if price_i in days:
                for price_j in prices[idx+1::]:
                    print("price_i", price_i)
                    print("price_j", price_j)
                    if price_i < price_j:

                        print("pricej-pricei", price_j-price_i)
                        value = max(value, price_j-price_i)
                        print("value", value)
                        # days[idx] = days.get(idx, value)
                        days[idx] = value
                        # {current_idx,value}
        maxValue = 0
        print("days", days)
        for day in days:
            maxValue = max(days[day], maxValue)
        return maxValue


print(Solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
# Expected 4
