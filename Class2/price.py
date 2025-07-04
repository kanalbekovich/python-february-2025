discount=0

def calculate_tax(price):
    tax = price * 0.08
    return tax

def apply_discount(price, discount):
    discount_sum = price * (discount/100)
    return discount_sum

price=float(input("Enter the price: "))
tax=calculate_tax(price)

# price 0-99 - no, 100-199 - 10%, 200+ 20%
if price >= 100 and price < 200:
    x=apply_discount(price, 10)
elif price >= 200:
    x=apply_discount(price, 20)
elif price < 100:
    x=apply_discount(price, 0)

total_price = price - x + tax
print(total_price)





