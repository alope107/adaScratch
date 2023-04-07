def max_profit(arr):
    reversed = sorted(arr, reverse=True)
    if arr == reversed:
        return 0
        
    profits= []
    
    for i in range(len(arr)-1):
        for j in range(i + 1,len(arr)):
            profit = arr[j] - arr[i]
            if profit > 0:
                profits.append((profit, i, j))

    
    #print(profits)
    profit_amts = []            
    for p in range(len(profits)-1):
        for q in range(p+1, len(profits)):
            profit = profits[p][0]
            if profits[q][1] > profits[p][2]:
                profit += profits[q][0]
            profit_amts.append(profit)

    #print(len(profit_amts))
                
    return max(profit_amts)
    # second solution, better time complexity
    # def max_profit(arr):
    #     profits = 0
    #     for i in range(1, len(arr)):
    #         profit = arr[i] - arr[i-1]
    #         if profit > 0:
    #             profits += profit
    #     return profit 
    
def max_profit_correct(prices):
    total_profit = 0
    for i in range(1, len(prices)):
        # if prices[i] - prices[i-1] is > 0, then we have a profit
        total_profit += max(prices[i]-prices[i-1], 0)
    return total_profit

# print(max_profit([3, 1, 1, 1, 5]))
# print(max_profit([3, 1, 1, 1, 3]))
# print(max_profit([1, 2, 3, 4, 5]))
# print(max_profit(list(range(100))))
print(max_profit([1, 2, 1, 2, 1, 2]))
print(max_profit_correct([1, 2, 1, 2, 1, 2]))
# print(max_profit([1, 2, 3, 2, 5, 4, 3, 1, 9, 5, 6, 7]))