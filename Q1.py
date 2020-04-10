"""
Ruize Zhang
4/9/2020
Calculate the maximum drawdown of a daily profit and loss sequence. Assume that the date series and the corresponding profit and loss series are stored in the dates and pnl arrays, respectively
5 days in total
Every day there are 10 elements of random (-1000 ~ 1000) pnl
The default starting value is 10
"""
import random
dates = ["4.9","4.10","4.11","4.12","4.13"]
initvalue = 10

#Calculate the maximum drawdown
for i in dates:
    pnl = []
    #Generate random pnl
    for j in range(10):
        profitchange = random.randrange(-1000,1000)
        pnl.append(profitchange)
    print(i,":",pnl)
    peak = trough = initvalue
    drawdown = max_drawdown = 0
    current = initvalue
    #calculating the drawdown of each segment of the day, and get the maximum value
    for num in range(len(pnl)):
        current += pnl[num]
        if current >= peak and peak != 0 or num == (len(pnl)-1):
            #If it is always falling, you need to calculate drawdown at the end
            if num == (len(pnl)-1):
                if current < trough:
                    trough = current
            drawdown = (peak-trough)/peak
            if drawdown > max_drawdown:
                max_drawdown = drawdown
            peak = current
            trough = peak
        elif current < trough:
            trough = current
    print("max drawdown: ", max_drawdown)





