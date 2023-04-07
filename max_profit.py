def max_profit(arr):
    profit = 0
    buyPrice = None
    for i in range(len(arr)):
        # Sell on last day if we have something
        if i == len(arr) - 1:
            if buyPrice is not None:
                profit += arr[i] - buyPrice
            break
        
        # If we don't have anything, only buy if it'll go up next
        if buyPrice is None and arr[i+1] > arr[i]:
            buyPrice = arr[i]
        
        # If we have something, only sell if it'll go down next    
        if buyPrice is not None:
            if arr[i+1] < arr[i]:
                profit += arr[i] - buyPrice
                buyPrice = None
    return profit