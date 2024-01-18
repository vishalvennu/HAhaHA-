def maxProfit(prices):
    minimum=min(prices)
    for i in range(len(prices)):
        if prices[i] == minimum:
            prices = prices[i:]
            break
    maximum=max(prices)
    for i in range(len(prices)):
        if prices[i] == maximum and i > 0:
            return prices[i] - prices[0]
    return 0

def maxProfit2(prices): # need to start from the left
    min_value = prices[0]
    
    return 0

prices = [2,4,1]

print(maxProfit(prices))
            
    
