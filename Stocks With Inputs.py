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
#Input Statements
amountPaidForStock = float(input("Enter amount paid for stock: "))
purchaseCommission = float(input("Enter commission paid on the purchase: "))
totalPaid = float(input("Enter total paid: "))
stockSoldFor = float(input("Enter amount the stock sold for: "))
sellingCommission = float(input("Enter commission paid on the sale: "))
totalReceived = float(input("Enter total received: "))
profitOrLoss = float(input("Enter profit (or loss if negative): "))
#Display
print ("Amount paid for stock: $", amountPaidForStock)
print ("Commission paid on the purchase: $", purchaseCommission)
print ("Amount the stock sold for: $", stockSoldFor)
print ("Commission paid on the sale: $", sellingCommission)
print ("Profit (or loss if negative): $", profitOrLoss)
