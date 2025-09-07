#
# Victor Byrd
# 9/6/2025
# Sales Tax Programming Project
# COSC 1010
#


# Calculate the state sales tax.
def calculateStateTax(purchase_Amount): 
    #state tax variable
    statetax=.05
    return purchase_Amount*statetax

def calculateCountyTax(purchase_Amount):
    #county tax variable
    countyTax=.025
    return purchase_Amount*countyTax

def displayTotals(purchase_Amount):
    print('purchase amount',purchase_Amount)
    statetax=calculateStateTax(purchase_Amount)
    print('state tax',statetax)
    countyTax=calculateCountyTax(purchase_Amount)
    print('county tax',countyTax)
    print('total',purchase_Amount+statetax+countyTax)

def main():
    purchase_Amount=float(input('enter the purchase amount:'))
    displayTotals(purchase_Amount)

main()