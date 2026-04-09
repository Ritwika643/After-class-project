import matplotlib.pyplot as plt

selling_price_mango=[515,700,892,421,389,654,741,910,805,345,479,789,623]
cost_price_mango = [256,475,961,654,378,845,216,856,719,523,413,352,851]

type= [selling_price_mango, cost_price_mango ]
colors=['darkblue','blue']
label=['selling price', 'cost price']
bins = [300,500,750,1000]
plt.xlabel('selling price')
plt.ylabel("cost price")
#amount range
#300-500 = low
#500-750 = moderate
#above 750 = high

plt.hist(type , bins = bins , width=0.95, color = colors,
         label = label, orientation="horizontal")

plt.title("Mango Amount")
plt.legend()
plt.show()