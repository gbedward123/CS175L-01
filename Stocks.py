#Gillian Bedward
#Stock
#Inputs
numShares = 2000
purchasePrice = 40.00
sellingPrice = 42.75
commissionRate = 0.03
#Calculations
amountPaidForStock = numShares * purchasePrice
purchaseCommission = commissionRate * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = numShares * sellingPrice
sellingCommission = commissionRate * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid
#Display
print ("Amount paid for stock: $", amountPaidForStock)
print ("Commission paid on the purchase: $", purchaseCommission)
print ("Amount the stock sold for: $", stockSoldFor)
print ("Commission paid on the sale: $", sellingCommission)
print ("Profit (or loss if negative): $", profitOrLoss)
